from twitter import compilar_contenido_apertura, compilar_contenido_cierre, tweetear_diario
from utilsMail import enviar_resumen_apertura,enviar_resumen_cierre, enviarAvisoDeCruce
from config import tickers

def ejecutarApertura():
    enviar_resumen_apertura(tickers)
    tweet_apertura=compilar_contenido_apertura(tickers)
    tweetear_diario(tweet_apertura)
    
if __name__ == "__main__":
    ejecutarApertura()