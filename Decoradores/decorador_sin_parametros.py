"""
Crear un decorador que imprima un mensaje antes y después de la ejecución de una función.
El decorador debe aplicarse a una función que sume dos números.
"""

# Definimos el decorador sin parámetros
def mi_decorador(func):
    # Definimos la función envolvente 'wrapper'
    def wrapper(*args, **kwargs):
        print("Ejecutando la función...")  # Mensaje antes de la ejecución
        resultado = func(*args, **kwargs)  # Llamamos a la función original
        print("Función ejecutada.")  # Mensaje después de la ejecución
        return resultado  # Retornamos el resultado de la función original
    return wrapper  # Retornamos la función envolvente

# Aplicamos el decorador a la función 'sumar'
@mi_decorador
def sumar(a, b):
    """Función que suma dos números."""
    return a + b

# Prueba la función
print(sumar(5, 3))


"""
- Decorador mi_decorador: Es una función que recibe otra función func y 
retorna una nueva función wrapper que añade comportamiento adicional.

- Función wrapper: Imprime un mensaje antes y después de ejecutar la 
función original func, sin modificar su lógica interna.

- Uso del decorador: Al usar @mi_decorador antes de la definición de 
sumar, estamos aplicando el decorador a esta función.

- Ejecución: Al llamar a sumar(5, 3), en realidad se ejecuta 
wrapper(5, 3), que a su vez llama a func(5, 3) (es decir, sumar(5, 3)).
"""