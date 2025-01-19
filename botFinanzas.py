import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import pandas as pd
import matplotlib.pyplot as plt
from dolar import *
from mail import *
from utilsMail import *
from utilsAcciones import *
from tareasProgramadas import *

# Lista de acciones a monitorear
acciones = ['AAPL', 'GOOGL', 'AMZN', "IBM", "META", "MSFT"]


obtenerMediaMovilExponencial("AAPL",200)
obtenerMediaMovilSimple("AAPL",200)

#print("Bot en ejecución...")
#while True:
#ejecutarTareasProgramadas()
    #time.sleep(1)






