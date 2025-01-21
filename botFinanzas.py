from utilsMail import *
from twitter import *
    
def ejecutarApertura():
    enviar_resumen_apertura()

def ejecutarCierre():
    enviar_resumen_cierre()
    enviarAvisoDeCruce()
    
    
enviarAvisoDeCruce()