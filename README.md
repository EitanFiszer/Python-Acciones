# Proyecto: Bot de Monitoreo de Acciones y Dólar

Este proyecto es un bot que monitorea las cotizaciones diarias de algunas acciones de empresas y los tipos de cambio del dólar (blue y contado con liqui), y envía un resumen por correo electrónico al final de la jornada de trading. El bot también obtiene la variación diaria de las acciones y el tipo de cambio del dólar, proporcionando esta información a través de correos electrónicos automáticos.

## Funcionalidades

1. **Monitoreo de Acciones**: El bot obtiene los precios de apertura y cierre de las acciones de las empresas seleccionadas como `AAPL`, `GOOGL`, `AMZN`, `IBM`, `META`, `MSFT`. Además, calcula la variación porcentual entre el precio de apertura y cierre de cada acción.

2. **Monitoreo del Dólar**: Se obtiene el precio de compra y venta del dólar en el mercado **blue** y **contado con liqui** utilizando una API pública.

3. **Envío de Correos Electrónicos**: Al final de la jornada de mercado (horarios configurables), el bot envía un correo electrónico con el resumen de las acciones monitoreadas, incluyendo su apertura, cierre y la variación porcentual. Además, incluye el tipo de cambio del dólar.

4. **Programación**: El bot está programado para ejecutar las tareas automáticamente todos los días a la hora definida, utilizando la biblioteca `schedule` para programar las funciones.

---

## Requisitos

Para ejecutar este proyecto en tu máquina local, necesitarás instalar los siguientes paquetes:

1. **yfinance**: Para obtener los datos financieros de las acciones.
   ```bash
   pip install yfinance

2. **schedule**: Para programar la ejecución de las tareas automáticas.
    ```bash
   pip install schedule

3. **requests**:  Para hacer solicitudes HTTP a la API que proporciona el precio del dólar.
    ```bash
   pip install requests
