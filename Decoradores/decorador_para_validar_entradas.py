"""
Crea un decorador que verifique si los parámetros de
una función son positivos. Si alguno no lo es, debe lanzar una excepción.
"""

# Definimos el decorador
def validar_positivos(func):
    # Función envolvente que validará los parámetros
    def wrapper(*args, **kwargs):
        # Verificamos si algún argumento posicional es negativo
        if any(a < 0 for a in args if isinstance(a, (int, float))):
            raise ValueError("Todos los parámetros deben ser positivos")
        # Verificamos si algún argumento nombrado es negativo
        if any(v < 0 for v in kwargs.values() if isinstance(v, (int, float))):
            raise ValueError("Todos los parámetros deben ser positivos")
        return func(*args, **kwargs)  # Ejecutamos la función original
    return wrapper  # Retornamos la función envolvente

# Aplicamos el decorador
@validar_positivos
def multiplicar(a, b):
    """Función que multiplica dos números."""
    return a * b

# Prueba la función
print(multiplicar(5, 3))  # Funciona correctamente
# print(multiplicar(-1, 3))  # Lanza excepción

"""
- Decorador validar_positivos: Verifica que todos los parámetros 
sean números positivos antes de ejecutar la función.

- Función wrapper: Utiliza comprensiones y funciones integradas 
como any() para comprobar los argumentos.

- Uso del decorador: Al usar @validar_positivos, cualquier llamada 
a multiplicar con parámetros negativos resultará en una excepción.
"""