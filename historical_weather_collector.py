import pandas as pd
import requests
from datetime import datetime, timedelta
import time
from tqdm import tqdm
import os
from config import CAPITAL_CITIES

# Clé API Visual Crossing Weather
API_KEY = "U8GKCBUX7LL9NJVHTHACPVC9R"  # Il faudra remplacer par une vraie clé API

def get_historical_weather(city, country, start_date, end_date):
    """Récupérer les données météo historiques pour une ville"""
    base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
    # Formatage de la ville et du pays pour l'URL
    location = f"{city.replace(' ', '%20')}"
    url = f"{base_url}/{location}?unitGroup=metric&include=days&elements=datetime,temp&key={API_KEY}&startDateTime={start_date}&endDateTime={end_date}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Erreur API pour {city}, {country}: {response.status_code}")
            print(f"URL: {url}")  # Pour le débogage
            return None
    except Exception as e:
        print(f"Erreur lors de la requête pour {city}, {country}: {str(e)}")
        return None

def collect_historical_data():
    # Créer le dossier de données s'il n'existe pas
    os.makedirs('data/historical', exist_ok=True)
    
    # Calculer les dates
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=365*20)  # 20 ans en arrière
    
    # Dataframe pour stocker toutes les données
    all_data = []
    
    print("Collecte des données historiques pour chaque capitale...")
    for city_info in tqdm(CAPITAL_CITIES):
        city = city_info['city']
        country = city_info['country']
        
        # Récupérer les données historiques
        data = get_historical_weather(city, country, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        
        if data is None:
            print(f"Impossible de récupérer les données pour {city}, {country}")
            continue
            
        # Traiter les données
        if 'days' in data:
            for day in data['days']:
                all_data.append({
                    'date': day['datetime'],
                    'temperature': day['temp'],
                    'city': city,
                    'country': country
                })
    
    # Créer le DataFrame et sauvegarder les données
    if all_data:
        df = pd.DataFrame(all_data)
        
        # Convertir la colonne de température en chaîne avec virgule comme séparateur décimal
        df['temperature'] = df['temperature'].apply(lambda x: f"{x:.1f}".replace('.', ','))
        
        # Sauvegarder toutes les données
        df.to_csv('data/historical/historical_temperatures.csv', index=False, sep=';')
        
        # Calculer et sauvegarder les moyennes mondiales
        df['temperature'] = df['temperature'].str.replace(',', '.').astype(float)  # Reconvertir en float pour le calcul
        daily_means = df.groupby('date')['temperature'].mean().reset_index()
        daily_means['temperature'] = daily_means['temperature'].apply(lambda x: f"{x:.1f}".replace('.', ','))
        daily_means.to_csv('data/historical/global_historical_temperatures.csv', index=False, sep=';')
        
        print("\nDonnées historiques sauvegardées dans data/historical/historical_temperatures.csv")
        print("Moyennes mondiales journalières sauvegardées dans data/historical/global_historical_temperatures.csv")
        
        return df
    
    return None

if __name__ == "__main__":
    collect_historical_data()
