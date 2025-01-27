from twitter import compilar_contenido_cierre,crear_hilo
from utilsMail import enviar_resumen_cierre, enviarAvisoDeCruce
from config import tickers

def ejecutarCierre():
    enviar_resumen_cierre(tickers)
    enviarAvisoDeCruce(tickers)
    tweet_cierre=compilar_contenido_cierre(tickers)
    crear_hilo(tweet_cierre,"CIERRE DE LA BOLSA HOY")

if __name__ == "__main__":
    
    ejecutarCierre()