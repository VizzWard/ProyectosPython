import re # libreria para manejar expresiones regulares
from exceptions import InvalidInputNumber # custom exception

# 1. Recibir la lista de nombres, tanto en consola como por archivo.
# 2. Crear funciones para:
# 2.1. Ordenar alfabeticamente
# 2.2. Convertirlos a mayusculas o minusculas
# 3. Guardar los nombres en un archivo de texto

def menu() -> list:
    """
        Muestra un menú para seleccionar cómo agregar los nombres.

        Retorna:
            list: Una lista de nombres ingresados por el usuario o cargados desde un archivo.

        Raises:
            InvalidInputNumber: Si la opción seleccionada no es válida.
    """
    print('Como desea agregar los nombres? ')
    manejo_de_datos = int(input('1 - Por consola, 2- Por archivo \n'))
    if manejo_de_datos == 1:
        return ingreso_de_datos()
    elif manejo_de_datos == 2:
        return cargar_archivo()
    else:
        raise InvalidInputNumber

def ingreso_de_datos() -> list:
    """
        Recibe una cadena de nombres ingresada por el usuario y los convierte en una lista.

        Retorna:
            list: Una lista de nombres obtenidos de la entrada del usuario.
    """
    lista = input('Ingrese los nombres que desea guardar (separados por un -):')
    lista_nombres = re.split(' |,|-', lista)
    return lista_nombres


def cargar_archivo() -> list:
    """
        Carga una lista de nombres desde un archivo de texto.

        Retorna:
            list: Una lista de nombres leídos desde el archivo.

        Raises:
            FileNotFoundError: Si el archivo no se encuentra.
    """
    archivo = input("Ingrese el nombre del archivo (ej: nombre.txt): ")
    lista = []
    try:
        with open(archivo, 'r') as archivo:
            lista = [linea.strip() for linea in archivo]
    except FileNotFoundError:
        print("El archivo no existe.")
    return lista


def modificar_lista(lista: list) -> list or None:
    """
    Muestra un menú al usuario para aplicar modificaciones a una lista de nombres.

    Dependiendo de la opción seleccionada por el usuario, la función puede:
        1. Convertir todos los nombres a mayúsculas.
        2. Convertir todos los nombres a minúsculas.
        3. Ordenar los nombres alfabéticamente.
        4. Guardar la lista en un archivo de texto.
        5. Salir sin hacer cambios.

    Parámetros:
        lista (list): Una lista de nombres que se desea modificar.

    Retorna:
        list: La lista modificada, ya sea en mayúsculas, minúsculas o ordenada alfabéticamente.
        None: Si el usuario elige salir sin hacer cambios.

    Nota:
        - La opción 4 guarda la lista en un archivo, pero no retorna nada.
        - La función `transformar_lista` es utilizada para convertir los nombres.
    """
    print('Modificaciones disponibles:')
    menu = int(input('1. Mayúsculas | 2. Minuscules | 3. Ordenar Alfabéticamente | 4. Guardar la lista en un archivo .txt | 5. Salir \n'))

    if menu == 1:
        return transformar_lista(lista, str.upper)
    elif menu == 2:
        return transformar_lista(lista, str.lower)
    elif menu == 3:
        return ordenar_alfabeticamente(lista)
    elif menu == 4:
        guardar_lista(lista)
    elif menu == 5:
        return None


def transformar_lista(lista: list, transformacion: callable) -> list:
    """
    Aplica una transformación a cada elemento de una lista de nombres.

    Parámetros:
        lista (list): Lista de nombres que se desea modificar.
        transformacion (callable): Una función que define cómo transformar cada elemento de la lista.
                                   Puede ser, por ejemplo, `str.upper` o `str.lower`.

    Retorna:
        list: Una lista con los elementos modificados según la transformación aplicada.
    """
    return [transformacion(elemento) for elemento in lista]


def ordenar_alfabeticamente(lista: list) -> list:
    """
    Ordena alfabéticamente una lista de nombres.

    Parámetros:
        lista (list): Una lista de nombres que se desea ordenar.

    Retorna:
        list: Una nueva lista con los nombres ordenados alfabéticamente.
    """
    return sorted(lista)


def guardar_lista(lista: list) -> None:
    """
    Guarda la lista en un archivo pero no retorna nada.

    Parámetros:
        lista (list): Lista de nombres que se desea guardar.

    Retorna:
        None: Esta funcion no retorna ningun valor
    """
    nombre_archivo = input('Ingrese el nombre para el archivo: \n')
    with open(f'{nombre_archivo}.txt', 'w') as archivo:
        for nombre in lista:
            archivo.write(nombre + '\n')

    print('Lista guardada exitosamente.')


# Menu
nombres = []
while True:
    try:
        nombres = menu()
    except InvalidInputNumber as e:
        print(e.message)

    while True:
        print('')
        print(f'Valores cargados: {nombres}')
        nombres = modificar_lista(nombres)

        if nombres is None:
            break
    if nombres is None:
        print('Finalizando programa...')
        break