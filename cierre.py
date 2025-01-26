from twitter import compilar_contenido_apertura, compilar_contenido_cierre, tweetear_diario
from utilsMail import enviar_resumen_apertura,enviar_resumen_cierre, enviarAvisoDeCruce
from config import tickers

def ejecutarCierre():
    enviar_resumen_cierre(tickers)
    enviarAvisoDeCruce(tickers)
    tweet_cierre=compilar_contenido_cierre(tickers)
    tweetear_diario(tweet_cierre)

if __name__ == "__main__":
    
    ejecutarCierre()