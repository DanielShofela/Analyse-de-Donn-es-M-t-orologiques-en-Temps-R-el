# Global Weather Data Collection and Visualization System

This project implements a real-time weather data collection and visualization system for global capitals using Python and Power BI.

## Prerequisites
- Python 3.8+
- OpenWeatherMap API key
- Power BI Desktop
- Required Python packages (see requirements.txt)

## Project Structure
```
├── README.md
├── requirements.txt
├── config.py
├── weather_collector.py
├── data_processor.py
└── data/
    └── weather_data.csv
```

## Setup Instructions

1. **Get OpenWeatherMap API Key**
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key
   - Add the API key to config.py

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Data Collection**
   ```bash
   python weather_collector.py
   ```

4. **Set up Power BI Dashboard**
   - Open the provided Power BI template
   - Configure data source refresh settings to 5 minutes
   - Publish dashboard to Power BI service for real-time monitoring

## Features
- Real-time weather data collection from global capitals
- Automatic data updates every 5 minutes
- Temperature, humidity, pressure, and wind speed monitoring
- Interactive visualizations in Power BI
- Historical data tracking

## Data Structure
The system collects the following weather parameters:
- Temperature (°C)
- Humidity (%)
- Pressure (hPa)
- Wind Speed (m/s)
- Weather Description
- Timestamp
- City
- Country
