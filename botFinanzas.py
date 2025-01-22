from twitter import *
from utilsMail import *
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Acceso a las variables
acciones = os.getenv("TICKERS")

def ejecutarApertura():
    enviar_resumen_apertura(acciones)
    tweet_apertura=compilar_contenido_apertura(acciones)
    tweetear_diario(tweet_apertura)
    
def ejecutarCierre():
    enviar_resumen_cierre(acciones)
    enviarAvisoDeCruce(acciones)
    tweet_cierre=compilar_contenido_cierre(acciones)
    tweetear_diario(tweet_cierre)
    

ejecutarApertura()
    