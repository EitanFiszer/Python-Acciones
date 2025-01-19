import schedule
from utilsMail import *

def ejecutarTareasProgramadas():
    schedule.every().day.at("11:00").do(enviar_resumen_apertura)  # Cambia a la hora que desees
    schedule.every().day.at("18:00").do(enviar_resumen_cierre)   # Cambia a la hora que desees
