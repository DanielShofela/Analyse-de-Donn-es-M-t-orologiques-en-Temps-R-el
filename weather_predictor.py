import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from datetime import datetime, timedelta
from config import DATA_FILE, COLUMN_NAMES

class WeatherPredictor:
    def __init__(self):
        self.data_file = DATA_FILE
        self.model = None
        self.scaler = StandardScaler()
        self.city_encoder = LabelEncoder()
        self.country_encoder = LabelEncoder()
        self.features = [COLUMN_NAMES['humidity'], COLUMN_NAMES['pressure'], 
                        COLUMN_NAMES['wind_speed']]

    def prepare_data(self, df):
        """Préparer les données pour l'entraînement"""
        # Encoder les villes et pays
        df['city_encoded'] = self.city_encoder.fit_transform(df[COLUMN_NAMES['city']])
        df['country_encoded'] = self.country_encoder.fit_transform(df[COLUMN_NAMES['country']])
        
        # Créer des caractéristiques temporelles
        df['hour'] = df[COLUMN_NAMES['timestamp']].dt.hour
        df['day_of_week'] = df[COLUMN_NAMES['timestamp']].dt.dayofweek
        df['month'] = df[COLUMN_NAMES['timestamp']].dt.month
        
        # Ajouter toutes les caractéristiques
        features = self.features + ['city_encoded', 'country_encoded', 
                                  'hour', 'day_of_week', 'month']
        
        # Préparer X (features) et y (target)
        X = df[features]
        y = df[COLUMN_NAMES['temperature']]
        
        # Normaliser les features numériques
        numeric_features = self.features + ['hour', 'day_of_week', 'month']
        X[numeric_features] = self.scaler.fit_transform(X[numeric_features])
        
        return X, y

    def train_model(self, df):
        """Entraîner le modèle de prédiction global"""
        print("\n=== Entraînement du modèle global ===")
        
        # Préparer les données
        X, y = self.prepare_data(df)
        
        # Diviser les données en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Initialiser et entraîner le modèle
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Évaluer le modèle
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"\nPerformances du modèle global:")
        print(f"  - MSE: {mse:.2f}")
        print(f"  - R²: {r2:.2f}")
        
        # Sauvegarder le modèle et les encodeurs
        joblib.dump(self.model, 'models/weather_model.joblib')
        joblib.dump(self.scaler, 'models/weather_scaler.joblib')
        joblib.dump(self.city_encoder, 'models/city_encoder.joblib')
        joblib.dump(self.country_encoder, 'models/country_encoder.joblib')

    def predict_next_24h(self, df):
        """Prédire la température pour les prochaines 24 heures pour chaque ville"""
        if self.model is None:
            print("Le modèle n'est pas encore entraîné!")
            return None
            
        all_predictions = []
        
        # Pour chaque ville
        for city in df[COLUMN_NAMES['city']].unique():
            # Obtenir la dernière entrée pour cette ville
            city_df = df[df[COLUMN_NAMES['city']] == city]
            if len(city_df) == 0:
                continue
                
            last_entry = city_df.iloc[-1]
            
            # Prédire pour les prochaines 24 heures
            for hour in range(24):
                next_hour = last_entry[COLUMN_NAMES['timestamp']] + timedelta(hours=hour+1)
                
                # Créer un dictionnaire avec les dernières valeurs connues
                prediction_data = {
                    COLUMN_NAMES['city']: [city],
                    COLUMN_NAMES['country']: [last_entry[COLUMN_NAMES['country']]],
                    COLUMN_NAMES['humidity']: [last_entry[COLUMN_NAMES['humidity']]],
                    COLUMN_NAMES['pressure']: [last_entry[COLUMN_NAMES['pressure']]],
                    COLUMN_NAMES['wind_speed']: [last_entry[COLUMN_NAMES['wind_speed']]],
                    COLUMN_NAMES['timestamp']: [next_hour]
                }
                
                # Créer un DataFrame
                pred_df = pd.DataFrame(prediction_data)
                
                # Encoder les villes et pays
                pred_df['city_encoded'] = self.city_encoder.transform(pred_df[COLUMN_NAMES['city']])
                pred_df['country_encoded'] = self.country_encoder.transform(pred_df[COLUMN_NAMES['country']])
                
                # Ajouter les caractéristiques temporelles
                pred_df['hour'] = pred_df[COLUMN_NAMES['timestamp']].dt.hour
                pred_df['day_of_week'] = pred_df[COLUMN_NAMES['timestamp']].dt.dayofweek
                pred_df['month'] = pred_df[COLUMN_NAMES['timestamp']].dt.month
                
                # Préparer les features pour la prédiction
                features = self.features + ['city_encoded', 'country_encoded', 
                                         'hour', 'day_of_week', 'month']
                X_pred = pred_df[features]
                
                # Normaliser les features numériques
                numeric_features = self.features + ['hour', 'day_of_week', 'month']
                X_pred[numeric_features] = self.scaler.transform(X_pred[numeric_features])
                
                # Faire la prédiction
                temp_pred = self.model.predict(X_pred)[0]
                
                all_predictions.append({
                    'timestamp': next_hour,
                    'city': city,
                    'country': last_entry[COLUMN_NAMES['country']],
                    'temperature': temp_pred
                })
        
        # Créer un DataFrame avec toutes les prédictions
        predictions_df = pd.DataFrame(all_predictions)
        predictions_df.to_csv('data/temperature_predictions.csv', 
                            sep=';', decimal=',', encoding='utf-8', index=False)
        
        return predictions_df

def main():
    from data_processor import WeatherDataProcessor
    
    # Charger les données
    processor = WeatherDataProcessor()
    df = processor.load_data()
    
    if df is not None:
        # Créer et entraîner le modèle
        predictor = WeatherPredictor()
        print("\nEntraînement du modèle de prédiction...")
        predictor.train_model(df)
        
        # Faire des prédictions pour les prochaines 24 heures
        print("\nGénération des prédictions pour les prochaines 24 heures...")
        predictions = predictor.predict_next_24h(df)
        
        if predictions is not None:
            print("\nPrédictions de température pour les prochaines 24 heures:")
            print("=" * 80)
            # Grouper par ville pour un affichage plus clair
            for city in predictions['city'].unique():
                print(f"\nPrédictions pour {city}:")
                print("-" * 60)
                city_pred = predictions[predictions['city'] == city].head(24)  # Afficher seulement les premières 24h
                for _, row in city_pred.iterrows():
                    print(f"Date: {row['timestamp'].strftime('%Y-%m-%d %H:%M')} | "
                          f"Température prévue: {row['temperature']:.1f}°C")

if __name__ == "__main__":
    main()
