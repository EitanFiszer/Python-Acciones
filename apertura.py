from twitter import compilar_contenido_apertura,crear_hilo
from utilsMail import enviar_resumen_apertura
from config import tickers

def ejecutarApertura():
    enviar_resumen_apertura(tickers)
    tweet_apertura=compilar_contenido_apertura(tickers)
    crear_hilo(tweet_apertura,"APERTURA DE LA BOLSA HOY")
    
if __name__ == "__main__":
    ejecutarApertura()