import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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
    
    # Obtener datos históricos con un período mayor para cubrir medias móviles largas
    data = ticker.history(period="max", interval="1d", actions=True)  # Último año (ajusta según lo necesario)
    
    # Asegúrate de que no haya valores NaN en la columna 'Close'
    data = data.dropna(subset=['Close'])

    # Calcular la EMA del tipo que se pasa como argumento, usando adjust=True
    data[f'EMA_{tipo}'] = data['Close'].ewm(span=tipo, adjust=True).mean()

    # Mostrar las últimas filas con la EMA calculada
    print(data[['Close', f'EMA_{tipo}']].tail())
    
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
    

# Función para graficar los datos
def graficarDatos(data, tipo):
    # Graficar el precio de cierre y la SMA calculada
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Precio de Cierre', color='blue')
    plt.plot(data.index, data[f'SMA_{tipo}'], label=f'SMA {tipo}', color='red')
    plt.title(f'Precio de Cierre y SMA de {tipo} Días')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.grid()
    plt.show()
