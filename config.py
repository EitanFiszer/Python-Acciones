from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv("./config.env")

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

print(SMTP_SERVER)
print(SMTP_PORT)  # Valor predeterminado 587
print(EMAIL_SENDER)
print(EMAIL_PASSWORD)
print(EMAIL_RECEIVER)
