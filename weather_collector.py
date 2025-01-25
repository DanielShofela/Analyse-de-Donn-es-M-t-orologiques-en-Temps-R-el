import requests
import pandas as pd
import schedule
import time
from datetime import datetime, timedelta
import pytz
import os
from config import API_KEY, BASE_URL, CAPITAL_CITIES, WEATHER_TRANSLATIONS, COLUMN_NAMES, UPDATE_INTERVAL, DATA_FILE

class WeatherDataCollector:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
        self.cities = CAPITAL_CITIES
        
        # Créer le répertoire data s'il n'existe pas
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        
        # Définir le chemin pour le fichier des températures en temps réel
        self.realtime_file = os.path.join(os.path.dirname(DATA_FILE), 'realtime_temperatures.csv')
        
        # Initialiser ou charger les fichiers CSV
        if not os.path.exists(DATA_FILE):
            self.create_empty_dataframe(DATA_FILE)
        if not os.path.exists(self.realtime_file):
            self.create_empty_dataframe(self.realtime_file)

    def create_empty_dataframe(self, file_path):
        """Créer un DataFrame vide avec les colonnes appropriées"""
        df = pd.DataFrame(columns=list(COLUMN_NAMES.values()))
        df.to_csv(file_path, index=False, sep=';', encoding='utf-8')

    def kelvin_to_celsius(self, kelvin):
        """Convertir la température de Kelvin en Celsius"""
        return round(kelvin - 273.15, 2)

    def get_weather_data(self, city, country):
        """Récupérer les données météo pour une ville spécifique"""
        print(f"\n🌍 Récupération des données pour {city}, {country}...")
        
        params = {
            'q': f"{city},{country}",
            'appid': self.api_key
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Traduire la description météo
            weather_desc = data['weather'][0]['description']
            translated_desc = WEATHER_TRANSLATIONS.get(weather_desc, weather_desc)
            
            temp = self.kelvin_to_celsius(data['main']['temp'])
            print(f"✅ {city}: {temp}°C, {translated_desc}")
            
            return {
                COLUMN_NAMES['timestamp']: datetime.now(pytz.UTC).strftime('%Y-%m-%d %H:%M:%S'),
                COLUMN_NAMES['city']: city,
                COLUMN_NAMES['country']: country,
                COLUMN_NAMES['temperature']: temp,
                COLUMN_NAMES['humidity']: data['main']['humidity'],
                COLUMN_NAMES['pressure']: data['main']['pressure'],
                COLUMN_NAMES['wind_speed']: data['wind']['speed'],
                COLUMN_NAMES['weather_description']: translated_desc
            }
        except requests.exceptions.RequestException as e:
            print(f"❌ Erreur pour {city}: {str(e)}")
            return None

    def save_realtime_temperatures(self, data_list):
        """Sauvegarder uniquement les températures actuelles"""
        if data_list:
            df = pd.DataFrame(data_list)
            # Garder uniquement les colonnes pertinentes
            columns_to_keep = [
                COLUMN_NAMES['timestamp'],
                COLUMN_NAMES['city'],
                COLUMN_NAMES['country'],
                COLUMN_NAMES['temperature'],
                COLUMN_NAMES['weather_description']
            ]
            df = df[columns_to_keep]
            
            # Remplacer les points par des virgules pour les décimaux
            df[COLUMN_NAMES['temperature']] = df[COLUMN_NAMES['temperature']].apply(
                lambda x: str(x).replace('.', ',')
            )
            
            # Écraser le fichier existant avec les nouvelles données
            df.to_csv(self.realtime_file, index=False, sep=';', encoding='utf-8')
            print(f"\n💡 Températures en temps réel sauvegardées dans : {self.realtime_file}")

    def collect_all_weather_data(self):
        """Collecter les données météo pour toutes les villes et sauvegarder en CSV"""
        print(f"\n📊 Début de la collecte des données météo à {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📍 Nombre de villes à traiter : {len(self.cities)}")
        
        new_data = []
        success_count = 0
        error_count = 0
        
        for city_info in self.cities:
            data = self.get_weather_data(city_info['city'], city_info['country'])
            if data:
                new_data.append(data)
                success_count += 1
            else:
                error_count += 1
        
        if new_data:
            print("\n💾 Sauvegarde des données...")
            # Sauvegarder l'historique complet
            df = pd.DataFrame(new_data)
            numeric_cols = [COLUMN_NAMES['temperature'], COLUMN_NAMES['humidity'], 
                          COLUMN_NAMES['pressure'], COLUMN_NAMES['wind_speed']]
            for col in numeric_cols:
                df[col] = df[col].apply(lambda x: str(x).replace('.', ','))
            
            df.to_csv(DATA_FILE, mode='a', header=not os.path.exists(DATA_FILE), 
                     index=False, sep=';', decimal=',', encoding='utf-8')
            
            # Sauvegarder les températures en temps réel
            self.save_realtime_temperatures(new_data)
            
            print(f"\n✨ Collecte terminée !")
            print(f"   ✅ Succès : {success_count} villes")
            if error_count > 0:
                print(f"   ❌ Erreurs : {error_count} villes")
            print(f"   📁 Historique complet : {DATA_FILE}")

def main():
    collector = WeatherDataCollector()
    
    def job():
        collector.collect_all_weather_data()
        # Calculer et afficher la prochaine exécution
        next_run = datetime.now() + timedelta(minutes=UPDATE_INTERVAL)
        print(f"\n⏰ Prochaine collecte prévue à : {next_run.strftime('%Y-%m-%d %H:%M:%S')}")
        print("..." * 30)

    # Exécuter immédiatement une première fois
    print("🚀 Démarrage du système de collecte météo")
    job()
    
    # Planifier les exécutions suivantes
    schedule.every(UPDATE_INTERVAL).minutes.do(job)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Arrêt du système de collecte")
        print("Au revoir !")

if __name__ == "__main__":
    main()
