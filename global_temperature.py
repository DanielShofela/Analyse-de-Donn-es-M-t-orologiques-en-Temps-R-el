import pandas as pd
from datetime import datetime

def calculate_global_temperature():
    # Lire le fichier CSV
    df = pd.read_csv('data/temperature_predictions.csv', sep=';')
    
    # Convertir la colonne temperature en remplaçant les virgules par des points
    df['temperature'] = df['temperature'].str.replace(',', '.').astype(float)
    
    # Convertir la colonne timestamp en datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Extraire la date (sans l'heure) pour le regroupement
    df['date'] = df['timestamp'].dt.date
    
    # Calculer la moyenne de température par jour
    daily_avg = df.groupby('date')['temperature'].mean().reset_index()
    
    # Sauvegarder les résultats dans un fichier CSV
    def save_to_csv(weather_data):
        """Sauvegarde les données météo dans un fichier CSV."""
        # Convertir les données en DataFrame
        df = pd.DataFrame(weather_data)
        
        # Convertir les valeurs numériques en chaînes avec virgule comme séparateur décimal
        numeric_columns = ['temperature']
        for col in numeric_columns:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: f"{x:.1f}".replace('.', ',') if pd.notnull(x) else '')
        
        # Sauvegarder en CSV
        df.to_csv('data/global_temperature_daily.csv', index=False, sep=';')
        print("\nDonnées sauvegardées dans data/global_temperature_daily.csv")
    
    save_to_csv(daily_avg)
    
    print("\nTempérature mondiale moyenne par jour:")
    for _, row in daily_avg.iterrows():
        print(f"Date: {row['date']} - Température moyenne: {row['temperature']:.2f}°C")
    
    return daily_avg

if __name__ == "__main__":
    calculate_global_temperature()
