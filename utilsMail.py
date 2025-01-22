import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utilsAcciones import *
from dolar import *
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Acceso a las variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # Valor predeterminado 587
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

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
    
    
        
def enviar_resumen_apertura(acciones):
    datos = obtener_datos_acciones(acciones)
    precios = obtener_precios_dolares()
    mensaje = "Resumen de apertura del mercado:\n\n"
    for accion, apertura, _, _ in datos:
        mensaje += f"{accion}: Apertura: ${apertura:.2f}\n"
    for tipo, datos in precios.items():
        mensaje += f"Dólar {tipo}: Compra: {datos['compra']}, Venta: {datos['venta']}\n"    
    enviar_correo("Apertura del mercado", mensaje)
    

def enviar_resumen_cierre(acciones):
    datos = obtener_datos_acciones(acciones)
    mensaje = "Resumen de cierre del mercado:\n\n"
    for accion, apertura, cierre, variacion in datos:
        mensaje += f"{accion}: Apertura: ${apertura:.2f}, Cierre: ${cierre:.2f}, Variación: {variacion:.2f}%\n"
    enviar_correo("Cierre del mercado", mensaje)
    
def enviarAvisoDeCruce(acciones):
    medias = [20, 50, 100, 200]
    avisos = []

    for accion in acciones:
        for i in range(len(medias)):
            for j in range(i + 1, len(medias)):
                media1 = medias[i]
                media2 = medias[j]
                
                if cruceDeMedias(accion, media1, media2):
                    aviso = f"¡Cruce detectado en {accion} entre EMA {media1} y EMA {media2}!"
                    avisos.append(aviso)
                    print(aviso)
    
    if avisos:
        # Construir el mensaje del correo
        mensaje = "Se detectaron los siguientes cruces de medias móviles:\n\n"
        mensaje += "\n".join(avisos)
        
        # Enviar el correo
        enviar_correo("Avisos de cruces de medias móviles", mensaje)
    else:
        print("No hubo cruces")
