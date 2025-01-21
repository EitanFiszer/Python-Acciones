import tweepy
from utilsAcciones import *
import config

#Autenticación con Twitter API
client = tweepy.Client(config.bearer_token,config.api_key,config.api_secret,config.access_token,config.access_token_secret)
auth = tweepy.OAuthHandler(config.api_key,config.api_secret,config.access_token,config.access_token_secret)
api = tweepy.API(auth)


def compilar_contenido_cierre(acciones):
    #Funcion para obtener el precio de una accion
    acciones = obtener_datos_acciones(acciones)
    tweet = ""
    for accion in acciones:
        nombre, apertura, cierre, variacion = accion
        tweet += f"{nombre}: Apertura:{apertura:.2f} Cierre:{cierre:.2f} Variación:{variacion:.2f}%\n"
    return tweet

def compilar_contenido_apertura(acciones):
    #Funcion para obtener el precio de una accion
    acciones = obtener_datos_acciones(acciones)
    tweet = ""
    for accion in acciones:
        nombre, apertura, cierre, variacion = accion
        tweet += f"{nombre}: Apertura:{apertura:.2f}\n"
    return tweet

def dividir_en_bloques(texto, lineas_por_bloque=4):
    """Divide un texto en bloques de n líneas."""
    lineas = texto.strip().split('\n')
    bloques = ['\n'.join(lineas[i:i + lineas_por_bloque]) for i in range(0, len(lineas), lineas_por_bloque)]
    return bloques


#Funcion para twittear lo que haga falta
def tweetear(contenido):
    client.create_tweet(text=contenido)