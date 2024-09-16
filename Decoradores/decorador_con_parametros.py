"""
Crear un decorador que acepte parámetros.
Debe permitir especificar cuántas veces se ejecutará la función decorada.
"""

# Definimos un decorador que acepta parámetros
def repetir(n):
    # Este es el decorador real
    def decorador(func):
        # Función envolvente que ejecutará 'func' 'n' veces
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)  # Llamamos a la función original
        return wrapper  # Retornamos la función envolvente
    return decorador  # Retornamos el decorador que acepta 'func'

# Aplicamos el decorador con el parámetro 'n'
@repetir(3)
def saludar(nombre):
    """Función que saluda a una persona."""
    print(f"Hola, {nombre}!")

# Prueba la función
saludar("Vicente")

"""
- Decorador con parámetros repetir(n): Es una función que recibe un 
argumento n y retorna un decorador.

- Decorador interno decorador: Recibe la función original func y 
retorna la función envolvente wrapper.

- Función wrapper: Ejecuta la función original func un total de n veces.

- Uso del decorador: Al usar @repetir(3), estamos indicando que queremos 
que la función saludar se ejecute 3 veces cada vez que es llamada.
"""