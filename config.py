import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8159881433:AAGYs-_e23agFL9tsoA2aO2q8Jai0ULECMU1")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "296319861"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1e7dcef8cb0d5358a6fb92d33e3db0631")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1938805245"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://kurd87709:VvKzGj3skdICo7yV@cluster0.hydya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "kurd87709")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
