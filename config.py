from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
if not load_dotenv("./config.env"):
    print("Advertencia: No se pudo cargar el archivo config.env")
    
tickers = os.getenv("TICKERS")
if tickers:
    tickers = tickers.split(",")  # Divide la cadena en una lista
else:
    tickers = []

bearer_token = os.getenv("bearer_token")
api_key = os.getenv("api_key")
api_secret = os.getenv("api_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")  # Valor predeterminado 587
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

