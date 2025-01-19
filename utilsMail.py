from mail import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utilsAcciones import *
from dolar import *

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