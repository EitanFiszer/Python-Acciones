from twitter import compilar_contenido_apertura, compilar_contenido_cierre, tweetear_diario
from utilsMail import enviar_resumen_apertura,enviar_resumen_cierre, enviarAvisoDeCruce
from config import tickers

# Acceso a las variables

print(tickers)

def ejecutarApertura():
    enviar_resumen_apertura(tickers)
    tweet_apertura=compilar_contenido_apertura(tickers)
    tweetear_diario(tweet_apertura)
    
def ejecutarCierre():
    enviar_resumen_cierre(tickers)
    enviarAvisoDeCruce(tickers)
    tweet_cierre=compilar_contenido_cierre(tickers)
    tweetear_diario(tweet_cierre)
    

ejecutarCierre()
    