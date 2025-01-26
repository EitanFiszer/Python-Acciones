import yfinance as yf
import pandas as pd
from grafico import *

# Devuelve una lista con los datos de las acciones
def obtener_datos_acciones(acciones):
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


def obtenerMediaMovilExponencial(accion, tipo):
    ticker = yf.Ticker(accion)  # Acción como parámetro
    
    # Obtener datos históricos
    data = ticker.history(period="10y", interval="1d", actions=True)
    
    # Asegúrate de que no haya valores NaN en la columna 'Close'
    data = data.dropna(subset=['Close'])

    # Calcular la EMA del tipo que se pasa como argumento
    data[f'EMA_{tipo}'] = data['Close'].ewm(span=tipo, adjust=True).mean()

    # Obtener los dos últimos valores de la EMA
    ultimos_emas = data[f'EMA_{tipo}'].iloc[-2:].tolist()

    return ultimos_emas
    
    #graficarDatos(data, tipo)


def obtenerMediaMovilSimple(accion, tipo):
    # Obtener datos históricos de la acción
    ticker = yf.Ticker(accion)
    datos = ticker.history(period="max",interval="1d")  # Obtener el historial máximo de datos disponibles
    
    # Asegúrate de que no haya valores NaN en la columna 'Close'
    datos = datos.dropna(subset=['Close'])
    
    # Calcular la SMA de 200 días (o el número de días que desees)
    datos[f'SMA_{tipo}'] = datos['Close'].rolling(window=tipo).mean()
    
    # Verificar que la SMA ha sido calculada correctamente
    print(datos[['Close', f'SMA_{tipo}']].tail())
    
    #graficarDatos(datos, tipo)
    
    
def cruceDeMedias(accion, media1, media2):
    # Obtener los últimos dos valores de las EMAs para ambas medias
    emas1 = obtenerMediaMovilExponencial(accion, media1)
    emas2 = obtenerMediaMovilExponencial(accion, media2)
    
    # Verificar si hay un cruce entre las medias
    return (emas1[0] < emas2[0] and emas1[1] > emas2[1]) or \
           (emas1[0] > emas2[0] and emas1[1] < emas2[1])
    
