import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from config import DATA_FILE, COLUMN_NAMES
import os

class WeatherDataProcessor:
    def __init__(self):
        self.data_file = DATA_FILE

    def load_data(self):
        """Charger et valider les données météo"""
        try:
            # Charger les données avec point-virgule comme séparateur
            df = pd.read_csv(self.data_file, sep=';', encoding='utf-8')
            df[COLUMN_NAMES['timestamp']] = pd.to_datetime(df[COLUMN_NAMES['timestamp']])
            
            # Convertir les colonnes numériques
            numeric_columns = [COLUMN_NAMES['temperature'], COLUMN_NAMES['humidity'], 
                             COLUMN_NAMES['pressure'], COLUMN_NAMES['wind_speed']]
            for col in numeric_columns:
                # Remplacer les virgules par des points et convertir en float
                df[col] = df[col].astype(str).str.replace(',', '.').astype(float)
            
            return df
        except Exception as e:
            print(f"Erreur lors du chargement des données : {str(e)}")
            return None

    def calculate_country_statistics(self, df):
        """Calculer les statistiques de température par pays"""
        print("\n=== Statistiques de température par pays ===")
        
        country_stats = df.groupby(COLUMN_NAMES['country']).agg({
            COLUMN_NAMES['temperature']: ['mean', 'min', 'max', 'std']
        }).round(2)
        
        # Renommer les colonnes pour plus de clarté
        country_stats.columns = [
            'Température moyenne (°C)',
            'Température minimale (°C)',
            'Température maximale (°C)',
            'Écart-type (°C)'
        ]
        
        # Trier par température moyenne décroissante
        country_stats = country_stats.sort_values('Température moyenne (°C)', ascending=False)
        
        # Afficher les statistiques avec un formatage agréable
        print("\nTop 5 pays les plus chauds :")
        print("=" * 50)
        for idx, (country, row) in enumerate(country_stats.head().iterrows(), 1):
            print(f"{idx}. {country}")
            print(f"   * Moyenne : {row['Température moyenne (°C)']:>6.1f}°C")
            print(f"   * Min/Max : {row['Température minimale (°C)']:>6.1f}°C / {row['Température maximale (°C)']:>6.1f}°C")
            print(f"   * Écart-type : {row['Écart-type (°C)']:>6.1f}°C")
            print("   " + "-" * 40)
        
        print("\nTop 5 pays les plus froids :")
        print("=" * 50)
        for idx, (country, row) in enumerate(country_stats.tail().iterrows(), 1):
            print(f"{idx}. {country}")
            print(f"   * Moyenne : {row['Température moyenne (°C)']:>6.1f}°C")
            print(f"   * Min/Max : {row['Température minimale (°C)']:>6.1f}°C / {row['Température maximale (°C)']:>6.1f}°C")
            print(f"   * Écart-type : {row['Écart-type (°C)']:>6.1f}°C")
            print("   " + "-" * 40)
        
        return country_stats

    def save_global_temperature_daily(self, df):
        # Créer le dossier data s'il n'existe pas
        os.makedirs('data', exist_ok=True)
        
        # Convertir les températures en chaînes avec virgule comme séparateur décimal
        df[COLUMN_NAMES['temperature']] = df[COLUMN_NAMES['temperature']].apply(lambda x: f"{x:.1f}".replace('.', ','))
        
        # Sauvegarder en CSV
        df.to_csv('data/global_temperature_daily.csv', index=False, sep=';')

    def process_data(self):
        """Fonction principale de traitement"""
        df = self.load_data()
        if df is None:
            return None
        
        # Calculer et sauvegarder les statistiques par pays
        country_stats = self.calculate_country_statistics(df)
        country_stats.to_csv('data/country_temperature_stats.csv', sep=';', decimal=',', encoding='utf-8')
        
        # Sauvegarder les températures quotidiennes
        self.save_global_temperature_daily(df)
        
        return country_stats

def main():
    processor = WeatherDataProcessor()
    results = processor.process_data()
    
    if results is not None:
        print("\nTraitement des données terminé")

if __name__ == "__main__":
    main()
