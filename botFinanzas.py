from twitter import *
import config

acciones = config.TICKERS

# Generar los tweets de cierre y apertura
tweet_cierre = compilar_contenido_cierre(acciones)
tweet_apertura = compilar_contenido_apertura(acciones)

# Dividir en bloques de 4 líneas
tweets_cierre = dividir_en_bloques(tweet_cierre, 4)
tweets_apertura = dividir_en_bloques(tweet_apertura, 4)

# Imprimir los bloques para verificar
#print("Tweets de cierre:")
#for tweet in tweets_cierre:
#    tweetear(tweet)
#
#print("Tweets de apertura:")
#for tweet in tweets_apertura:
#    tweetear(tweet)