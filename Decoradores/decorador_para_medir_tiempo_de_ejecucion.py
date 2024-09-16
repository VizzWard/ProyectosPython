"""
Crea un decorador que mida el tiempo de ejecución de una función.
"""

import time  # Importamos el módulo 'time' para medir el tiempo

# Definimos el decorador
def medir_tiempo(func):
    # Función envolvente que medirá el tiempo
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Tiempo antes de ejecutar la función
        resultado = func(*args, **kwargs)  # Ejecutamos la función original
        fin = time.time()  # Tiempo después de ejecutar la función
        print(f"Tiempo de ejecución: {fin - inicio} segundos")  # Mostramos el tiempo transcurrido
        return resultado  # Retornamos el resultado de la función original
    return wrapper  # Retornamos la función envolvente

# Aplicamos el decorador a la función 'contar_hasta_mil'
@medir_tiempo
def contar_hasta_mil():
    """Función que cuenta hasta mil."""
    for i in range(1000000000):
        pass  # Operación de paso (no hace nada)

# Prueba la función
contar_hasta_mil()

"""
- Decorador medir_tiempo: Mide el tiempo antes y después de ejecutar 
la función original para calcular el tiempo total de ejecución.

- Función wrapper: Se encarga de capturar el tiempo de inicio y fin, 
ejecutar la función original y mostrar el tiempo transcurrido.

- Uso del decorador: Al usar @medir_tiempo, cada vez que se llama a 
contar_hasta_mil, se mide y muestra cuánto tiempo tarda en ejecutarse.
"""