@echo off
echo Installation de l'environnement virtuel...
call venv\Scripts\activate.bat

echo Installation des packages...
pip install requests==2.31.0
pip install python-dotenv==1.0.0
pip install schedule==1.2.1
pip install pytz==2023.3
pip install --only-binary :all: pandas

echo Installation terminée !
pause
