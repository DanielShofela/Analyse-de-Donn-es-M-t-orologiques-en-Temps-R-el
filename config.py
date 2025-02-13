# OpenWeatherMap API Configuration
API_KEY = "9ba50cd0dccbd361337789326abb4058"  # Remplacez par votre clé API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Dictionnaire de traduction des conditions météo avec emojis
WEATHER_TRANSLATIONS = {
    # Groupe : Orage
    "thunderstorm with light rain": "Orage avec pluie légère ⛈️",
    "thunderstorm with rain": "Orage avec pluie ⛈️",
    "thunderstorm with heavy rain": "Orage avec forte pluie ⛈️",
    "light thunderstorm": "Orage léger 🌩️",
    "thunderstorm": "Orage 🌩️",
    "heavy thunderstorm": "Orage violent ⛈️",
    "ragged thunderstorm": "Orage irrégulier 🌩️",
    "thunderstorm with light drizzle": "Orage avec bruine légère 🌩️",
    "thunderstorm with drizzle": "Orage avec bruine 🌩️",
    "thunderstorm with heavy drizzle": "Orage avec forte bruine ⛈️",

    # Groupe : Bruine
    "light intensity drizzle": "Bruine légère 🌧️",
    "drizzle": "Bruine 🌧️",
    "heavy intensity drizzle": "Forte bruine 🌧️",
    "light intensity drizzle rain": "Bruine légère 🌧️",
    "drizzle rain": "Pluie bruineuse 🌧️",
    "heavy intensity drizzle rain": "Forte pluie bruineuse 🌧️",
    "shower rain and drizzle": "Averses et bruine 🌧️",
    "heavy shower rain and drizzle": "Fortes averses et bruine 🌧️",
    "shower drizzle": "Averses bruineuses 🌧️",

    # Groupe : Pluie
    "light rain": "Pluie légère 🌧️",
    "moderate rain": "Pluie modérée 🌧️",
    "heavy intensity rain": "Forte pluie 🌧️",
    "very heavy rain": "Très forte pluie 🌧️",
    "extreme rain": "Pluie extrême 🌧️",
    "freezing rain": "Pluie verglaçante 🌧️",
    "light intensity shower rain": "Averses légères 🌦️",
    "shower rain": "Averses 🌦️",
    "heavy intensity shower rain": "Fortes averses 🌦️",
    "ragged shower rain": "Averses irrégulières 🌦️",

    # Groupe : Neige
    "light snow": "Neige légère 🌨️",
    "snow": "Neige ❄️",
    "heavy snow": "Forte neige ❄️",
    "sleet": "Grésil 🌨️",
    "light shower sleet": "Légères averses de grésil 🌨️",
    "shower sleet": "Averses de grésil 🌨️",
    "light rain and snow": "Pluie et neige légères 🌨️",
    "rain and snow": "Pluie et neige 🌨️",
    "light shower snow": "Légères averses de neige 🌨️",
    "shower snow": "Averses de neige 🌨️",
    "heavy shower snow": "Fortes averses de neige ❄️",

    # Groupe : Atmosphère
    "mist": "Brume 🌫️",
    "smoke": "Fumée 🌫️",
    "haze": "Brume sèche 🌫️",
    "sand/dust whirls": "Tourbillons de sable/poussière 🌪️",
    "fog": "Brouillard 🌫️",
    "sand": "Sable 🌫️",
    "dust": "Poussière 🌫️",
    "volcanic ash": "Cendres volcaniques 🌋",
    "squalls": "Grains 🌪️",
    "tornado": "Tornade 🌪️",

    # Groupe : Nuages et ciel clair
    "clear sky": "Ciel dégagé ☀️",
    "few clouds": "Quelques nuages 🌤️",
    "scattered clouds": "Nuages épars ⛅",
    "broken clouds": "Nuages fragmentés 🌥️",
    "overcast clouds": "Ciel couvert ☁️"
}

# Noms des colonnes avec unités
COLUMN_NAMES = {
    "timestamp": "Horodatage",
    "city": "Ville",
    "country": "Pays",
    "temperature": "Température (°C)",
    "humidity": "Humidité (%)",
    "pressure": "Pression (hPa)",
    "wind_speed": "Vitesse du vent (m/s)",
    "weather_description": "Description météo"
}

# List of capital cities to monitor
CAPITAL_CITIES = [
    # Europe
    {"city": "Tirana", "country": "Albania"},
    {"city": "Berlin", "country": "Germany"},
    {"city": "Andorra la Vella", "country": "Andorra"},
    {"city": "Vienna", "country": "Austria"},
    {"city": "Brussels", "country": "Belgium"},
    {"city": "Minsk", "country": "Belarus"},
    {"city": "Sarajevo", "country": "Bosnia and Herzegovina"},
    {"city": "Sofia", "country": "Bulgaria"},
    {"city": "Nicosia", "country": "Cyprus"},
    {"city": "Zagreb", "country": "Croatia"},
    {"city": "Copenhagen", "country": "Denmark"},
    {"city": "Madrid", "country": "Spain"},
    {"city": "Tallinn", "country": "Estonia"},
    {"city": "Helsinki", "country": "Finland"},
    {"city": "Paris", "country": "France"},
    {"city": "Athens", "country": "Greece"},
    {"city": "Budapest", "country": "Hungary"},
    {"city": "Dublin", "country": "Ireland"},
    {"city": "Reykjavik", "country": "Iceland"},
    {"city": "Rome", "country": "Italy"},
    {"city": "Pristina", "country": "Kosovo"},
    {"city": "Riga", "country": "Latvia"},
    {"city": "Vaduz", "country": "Liechtenstein"},
    {"city": "Vilnius", "country": "Lithuania"},
    {"city": "Luxembourg", "country": "Luxembourg"},
    {"city": "Skopje", "country": "North Macedonia"},
    {"city": "Valletta", "country": "Malta"},
    {"city": "Chisinau", "country": "Moldova"},
    {"city": "Monaco", "country": "Monaco"},
    {"city": "Podgorica", "country": "Montenegro"},
    {"city": "Oslo", "country": "Norway"},
    {"city": "Amsterdam", "country": "Netherlands"},
    {"city": "Warsaw", "country": "Poland"},
    {"city": "Lisbon", "country": "Portugal"},
    {"city": "Prague", "country": "Czech Republic"},
    {"city": "Bucharest", "country": "Romania"},
    {"city": "London", "country": "United Kingdom"},
    {"city": "Moscow", "country": "Russia"},
    {"city": "San Marino", "country": "San Marino"},
    {"city": "Belgrade", "country": "Serbia"},
    {"city": "Bratislava", "country": "Slovakia"},
    {"city": "Ljubljana", "country": "Slovenia"},
    {"city": "Stockholm", "country": "Sweden"},
    {"city": "Bern", "country": "Switzerland"},
    {"city": "Kiev", "country": "Ukraine"},
    {"city": "Vatican City", "country": "Vatican City State"},

    # Asia
    {"city": "Kabul", "country": "Afghanistan"},
    {"city": "Riyadh", "country": "Saudi Arabia"},
    {"city": "Yerevan", "country": "Armenia"},
    {"city": "Baku", "country": "Azerbaijan"},
    {"city": "Manama", "country": "Bahrain"},
    {"city": "Dhaka", "country": "Bangladesh"},
    {"city": "Thimphu", "country": "Bhutan"},
    {"city": "Naypyidaw", "country": "Myanmar"},
    {"city": "Bandar Seri Begawan", "country": "Brunei"},
    {"city": "Phnom Penh", "country": "Cambodia"},
    {"city": "Beijing", "country": "China"},
    {"city": "Pyongyang", "country": "North Korea"},
    {"city": "Seoul", "country": "South Korea"},
    {"city": "Abu Dhabi", "country": "United Arab Emirates"},
    {"city": "Tbilisi", "country": "Georgia"},
    {"city": "New Delhi", "country": "India"},
    {"city": "Jakarta", "country": "Indonesia"},
    {"city": "Baghdad", "country": "Iraq"},
    {"city": "Tehran", "country": "Iran"},
    {"city": "Jerusalem", "country": "Israel"},
    {"city": "Tokyo", "country": "Japan"},
    {"city": "Amman", "country": "Jordan"},
    {"city": "Nur-Sultan", "country": "Kazakhstan"},
    {"city": "Bishkek", "country": "Kyrgyzstan"},
    {"city": "Kuwait City", "country": "Kuwait"},
    {"city": "Vientiane", "country": "Laos"},
    {"city": "Beirut", "country": "Lebanon"},
    {"city": "Kuala Lumpur", "country": "Malaysia"},
    {"city": "Male", "country": "Maldives"},
    {"city": "Ulaanbaatar", "country": "Mongolia"},
    {"city": "Kathmandu", "country": "Nepal"},
    {"city": "Muscat", "country": "Oman"},
    {"city": "Tashkent", "country": "Uzbekistan"},
    {"city": "Islamabad", "country": "Pakistan"},
    {"city": "Manila", "country": "Philippines"},
    {"city": "Doha", "country": "Qatar"},
    {"city": "Singapore", "country": "Singapore"},
    {"city": "Colombo", "country": "Sri Lanka"},
    {"city": "Damascus", "country": "Syria"},
    {"city": "Dushanbe", "country": "Tajikistan"},
    {"city": "Taipei", "country": "Taiwan"},
    {"city": "Bangkok", "country": "Thailand"},
    {"city": "Dili", "country": "East Timor"},
    {"city": "Ashgabat", "country": "Turkmenistan"},
    {"city": "Ankara", "country": "Turkey"},
    {"city": "Hanoi", "country": "Vietnam"},
    {"city": "Sanaa", "country": "Yemen"},

    # Africa
    {"city": "Pretoria", "country": "South Africa"},
    {"city": "Algiers", "country": "Algeria"},
    {"city": "Luanda", "country": "Angola"},
    {"city": "Porto-Novo", "country": "Benin"},
    {"city": "Gaborone", "country": "Botswana"},
    {"city": "Ouagadougou", "country": "Burkina Faso"},
    {"city": "Gitega", "country": "Burundi"},
    {"city": "Yaounde", "country": "Cameroon"},
    {"city": "Praia", "country": "Cape Verde"},
    {"city": "Moroni", "country": "Comoros"},
    {"city": "Brazzaville", "country": "Republic of Congo"},
    {"city": "Abidjan", "country": "Ivory Coast"},
    {"city": "Djibouti", "country": "Djibouti"},
    {"city": "Cairo", "country": "Egypt"},
    {"city": "Asmara", "country": "Eritrea"},
    {"city": "Mbabane", "country": "Eswatini"},
    {"city": "Addis Ababa", "country": "Ethiopia"},
    {"city": "Libreville", "country": "Gabon"},
    {"city": "Banjul", "country": "Gambia"},
    {"city": "Accra", "country": "Ghana"},
    {"city": "Conakry", "country": "Guinea"},
    {"city": "Malabo", "country": "Equatorial Guinea"},
    {"city": "Bissau", "country": "Guinea-Bissau"},
    {"city": "Nairobi", "country": "Kenya"},
    {"city": "Maseru", "country": "Lesotho"},
    {"city": "Monrovia", "country": "Liberia"},
    {"city": "Tripoli", "country": "Libya"},
    {"city": "Antananarivo", "country": "Madagascar"},
    {"city": "Lilongwe", "country": "Malawi"},
    {"city": "Bamako", "country": "Mali"},
    {"city": "Rabat", "country": "Morocco"},
    {"city": "Port Louis", "country": "Mauritius"},
    {"city": "Nouakchott", "country": "Mauritania"},
    {"city": "Maputo", "country": "Mozambique"},
    {"city": "Windhoek", "country": "Namibia"},
    {"city": "Niamey", "country": "Niger"},
    {"city": "Abuja", "country": "Nigeria"},
    {"city": "Kampala", "country": "Uganda"},
    {"city": "Bangui", "country": "Central African Republic"},
    {"city": "Kinshasa", "country": "Democratic Republic of the Congo"},
    {"city": "Kigali", "country": "Rwanda"},
    {"city": "Sao Tome", "country": "Sao Tome and Principe"},
    {"city": "Dakar", "country": "Senegal"},
    {"city": "Victoria", "country": "Seychelles"},
    {"city": "Freetown", "country": "Sierra Leone"},
    {"city": "Mogadishu", "country": "Somalia"},
    {"city": "Khartoum", "country": "Sudan"},
    {"city": "Juba", "country": "South Sudan"},
    {"city": "Dodoma", "country": "Tanzania"},
    {"city": "NDjamena", "country": "Chad"},
    {"city": "Lome", "country": "Togo"},
    {"city": "Tunis", "country": "Tunisia"},
    {"city": "Lusaka", "country": "Zambia"},
    {"city": "Harare", "country": "Zimbabwe"},

    # North America
    {"city": "Saint John's", "country": "Antigua and Barbuda"},
    {"city": "Nassau", "country": "Bahamas"},
    {"city": "Bridgetown", "country": "Barbados"},
    {"city": "Belmopan", "country": "Belize"},
    {"city": "Ottawa", "country": "Canada"},
    {"city": "San Jose", "country": "Costa Rica"},
    {"city": "Havana", "country": "Cuba"},
    {"city": "Roseau", "country": "Dominica"},
    {"city": "Washington", "country": "United States"},
    {"city": "Saint George's", "country": "Grenada"},
    {"city": "Guatemala City", "country": "Guatemala"},
    {"city": "Port-au-Prince", "country": "Haiti"},
    {"city": "Tegucigalpa", "country": "Honduras"},
    {"city": "Kingston", "country": "Jamaica"},
    {"city": "Mexico City", "country": "Mexico"},
    {"city": "Managua", "country": "Nicaragua"},
    {"city": "Panama City", "country": "Panama"},
    {"city": "Santo Domingo", "country": "Dominican Republic"},
    {"city": "Basseterre", "country": "Saint Kitts and Nevis"},
    {"city": "Kingstown", "country": "Saint Vincent and the Grenadines"},
    {"city": "Castries", "country": "Saint Lucia"},
    {"city": "San Salvador", "country": "El Salvador"},
    {"city": "Port of Spain", "country": "Trinidad and Tobago"},

    # South America
    {"city": "Buenos Aires", "country": "Argentina"},
    {"city": "La Paz", "country": "Bolivia"},
    {"city": "Brasilia", "country": "Brazil"},
    {"city": "Santiago", "country": "Chile"},
    {"city": "Bogota", "country": "Colombia"},
    {"city": "Quito", "country": "Ecuador"},
    {"city": "Georgetown", "country": "Guyana"},
    {"city": "Asuncion", "country": "Paraguay"},
    {"city": "Lima", "country": "Peru"},
    {"city": "Paramaribo", "country": "Suriname"},
    {"city": "Montevideo", "country": "Uruguay"},
    {"city": "Caracas", "country": "Venezuela"},

    # Oceania
    {"city": "Canberra", "country": "Australia"},
    {"city": "Suva", "country": "Fiji"},
    {"city": "Majuro", "country": "Marshall Islands"},
    {"city": "Honiara", "country": "Solomon Islands"},
    {"city": "South Tarawa", "country": "Kiribati"},
    {"city": "Palikir", "country": "Micronesia"},
    {"city": "Yaren", "country": "Nauru"},
    {"city": "Wellington", "country": "New Zealand"},
    {"city": "Ngerulmud", "country": "Palau"},
    {"city": "Port Moresby", "country": "Papua New Guinea"},
    {"city": "Apia", "country": "Samoa"},
    {"city": "Nuku'alofa", "country": "Tonga"},
    {"city": "Funafuti", "country": "Tuvalu"},
    {"city": "Port Vila", "country": "Vanuatu"}
]

# Data collection settings
UPDATE_INTERVAL = 300  # 5 minutes in seconds
DATA_FILE = "data/weather_data.csv"
