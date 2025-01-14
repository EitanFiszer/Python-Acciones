import yfinance as yf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
from dolar import *


##eeeee
# Configuración de correo
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "finanzasfc2@gmail.com"  # Tu correo Gmail
EMAIL_PASSWORD = "mcuz krwl lrhv mlrb"  # Genera una contraseña de aplicación
EMAIL_RECEIVER = "eitandfiszer@gmail.com"  # Correo que recibirá el resumen


# Lista de acciones a monitorear
acciones = ['AAPL', 'GOOGL', 'AMZN', "IBM", "META", "MSFT"]

# Obtene datos
def obtener_datos_acciones():
    """Obtiene los datos actuales de las acciones y calcula variaciones."""
    datos = []
    for accion in acciones:
        try:
            ticker = yf.Ticker(accion)
            historial = ticker.history(period="1d")
            if not historial.empty:
                apertura = historial['Open'].iloc[0]  # Corregido con .iloc
                cierre = historial['Close'].iloc[0]  # Corregido con .iloc
                variacion = ((cierre - apertura) / apertura) * 100
                datos.append((accion, apertura, cierre, variacion))
        except Exception as e:
            print(f"Error al obtener datos para {accion}: {e}")
    return datos


##Enviar correo
def enviar_correo(asunto, mensaje):
    """Envía un correo con el asunto y mensaje proporcionados."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = asunto

    # Cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    # Enviar correo
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar correo: {e}")



def enviar_resumen_apertura():
    """Envía el resumen cuando abre el mercado."""
    datos = obtener_datos_acciones()
    precios = obtener_precios_dolares()
    mensaje = "Resumen de apertura del mercado:\n\n"
    for accion, apertura, _, _ in datos:
        mensaje += f"{accion}: Apertura: ${apertura:.2f}\n"
    for tipo, datos in precios.items():
        mensaje += f"Dólar {tipo}: Compra: {datos['compra']}, Venta: {datos['venta']}\n"    
    enviar_correo("Apertura del mercado (prueba)", mensaje)



def enviar_resumen_cierre():
    """Envía el resumen cuando cierra el mercado."""
    datos = obtener_datos_acciones()
    mensaje = "Resumen de cierre del mercado:\n\n"
    for accion, apertura, cierre, variacion in datos:
        mensaje += f"{accion}: Apertura: ${apertura:.2f}, Cierre: ${cierre:.2f}, Variación: {variacion:.2f}%\n"
    enviar_correo("Cierre del mercado (prueba)", mensaje)





# Programar las tareas
schedule.every().day.at("17:23").do(enviar_resumen_apertura)  # Cambia a la hora que desees
schedule.every().day.at("17:25").do(enviar_resumen_cierre)   # Cambia a la hora que desees


print("Bot en ejecución...")
while True:
    schedule.run_pending()
    time.sleep(1)
