import matplotlib.pyplot as plt

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
