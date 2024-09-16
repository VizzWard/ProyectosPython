"""
Crea dos decoradores: uno que transforme el resultado de una función
a mayúsculas y otro que agregue signos de exclamación al resultado.
Usa ambos decoradores en una función.
"""

# Decorador que convierte el resultado a mayúsculas
def en_mayusculas(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)  # Ejecutamos la función original
        return resultado.upper()  # Convertimos el resultado a mayúsculas
    return wrapper  # Retornamos la función envolvente

# Decorador que agrega un signo de exclamación al resultado
def agregar_exclamacion(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)  # Ejecutamos la función original
        return f"{resultado}!"  # Agregamos el signo de exclamación
    return wrapper  # Retornamos la función envolvente

# Aplicamos ambos decoradores a la función 'saludar'
@en_mayusculas
@agregar_exclamacion
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"Hola, {nombre}"

# Prueba la función
print(saludar("Vicente"))

"""
- Decorador agregar_exclamacion: Añade un signo de exclamación 
al final del resultado de la función.

- Decorador en_mayusculas: Convierte el resultado de la función 
a mayúsculas.

- Anidación de decoradores: Se aplican de abajo hacia arriba. 
Primero agregar_exclamacion, luego en_mayusculas.
    - Paso 1: saludar("Carlos") retorna "Hola, Carlos".
    - Paso 2: agregar_exclamacion transforma esto en "Hola, Carlos!".
    - Paso 3: en_mayusculas convierte el resultado en "HOLA, CARLOS!".

- Uso de los decoradores: Al anidar los decoradores, 
combinamos sus efectos para transformar el resultado final.
"""