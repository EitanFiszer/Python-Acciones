import tweepy
from utilsAcciones import *
from config import bearer_token, api_key, api_secret, access_token, access_token_secret

#Autenticación con Twitter API
client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuthHandler(api_key,api_secret,access_token,access_token_secret)
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

################################### FUNCIONES EN DESUSO ###################################
#def tweetear_diario(tweet_diario):
#    tweets_diario = dividir_en_bloques(tweet_diario, 4)
#    for tweet in tweets_diario:
#        tweetear(tweet)
#    print("Tweeteado con exito")
#
##Funcion para twittear lo que haga falta
#def tweetear(contenido):
#    client.create_tweet(text=contenido)

#############################################################################################

def crear_hilo(tweet_diario, encabezado):
    # Dividir el contenido en bloques de 4 líneas
    tweets_diario = dividir_en_bloques(tweet_diario, 4)

    # Crear el contenido del primer tweet: encabezado + primeros 4 valores
    primer_tweet = f"{encabezado}\n\n{tweets_diario[0]}" if tweets_diario else encabezado

    # Publicar el primer tweet
    respuesta = client.create_tweet(text=primer_tweet)
    ultimo_tweet_id = respuesta.data['id']  # Obtener el ID del tweet inicial

    # Publicar los siguientes bloques como respuestas al último tweet publicado
    for tweet in tweets_diario[1:]:  # Excluir el primer bloque ya usado
        respuesta = client.create_tweet(text=tweet, in_reply_to_tweet_id=ultimo_tweet_id)
        ultimo_tweet_id = respuesta.data['id']  # Actualizar el ID del último tweet publicado
        print(f"Tweet publicado: {tweet}")
    
    print("Hilo publicado con éxito.")
