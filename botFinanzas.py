from utilsMail import *
from twitter import *
from config import *
        
def ejecutarApertura():
    enviar_resumen_apertura(TICKERS)

def ejecutarCierre():
    enviar_resumen_cierre(TICKERS)
    enviarAvisoDeCruce(TICKERS)
    
    
ejecutarApertura()
ejecutarCierre()