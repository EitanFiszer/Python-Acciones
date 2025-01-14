import requests

def obtener_precios_dolares():
    urls = [
    'https://dolarapi.com/v1/dolares/blue',
    'https://dolarapi.com/v1/dolares/contadoconliqui'
    ]
    
    precios = {}
    
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                
                nombre = data.get('nombre', 'Desconocido')
                compra = data.get('compra', 'No disponible')
                venta = data.get('venta', 'No disponible')
                
                # Guardar los resultados en el diccionario
                precios[nombre] = {'compra': compra, 'venta': venta}
            else:
                precios[url] = {'error': f"HTTP {response.status_code}"}
        except Exception as e:
            precios[url] = {'error': str(e)}
    
    return precios


precios = obtener_precios_dolares()

# Mostrar resultados
for tipo, datos in precios.items():
    if 'error' in datos:
        print(f"{tipo}: {datos['error']}")
    else:
        print(f"Dólar {tipo}: Compra: {datos['compra']}, Venta: {datos['venta']}")
