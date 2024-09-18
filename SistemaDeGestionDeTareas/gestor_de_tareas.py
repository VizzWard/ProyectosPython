import json
import os
import time

from exceptions import EndProgram, InvalidInputNumber, EndMenu
from datetime import datetime

def main_menu() -> None:
    """
    Función principal que maneja el bucle del menú principal y las excepciones globales.

    Esta función ejecuta un bucle infinito que muestra el menú principal y maneja
    varias excepciones que pueden ocurrir durante la ejecución del programa.

    Returns:
        None

    Raises:
        ValueError: Capturada internamente. Ocurre cuando se ingresa un valor no numérico.
        EndProgram: Capturada internamente. Señal para terminar el programa.
        FileNotFoundError: Capturada internamente. Ocurre cuando no se encuentra el archivo de tareas.
        InvalidInputNumber: Capturada internamente. Ocurre cuando se ingresa un número de opción inválido.

    Side Effects:
        - Interactúa con el usuario a través de la consola (input/output).
        - Puede crear un archivo JSON vacío si no existe.
        - Llama a otras funciones del programa.

    Note:
        Esta función depende de la existencia de las siguientes funciones y clases:
        - menu()
        - crear_json_vacio()
        - EndProgram (excepción personalizada)
        - InvalidInputNumber (excepción personalizada)
    """
    while True:
        try:
            menu()
        except ValueError as e:
            print('Ingrese un valor valido')
        except EndProgram as e:
            print(e)
            #time.sleep(2)
            break
        except FileNotFoundError as e:
            crear_json_vacio()
        except InvalidInputNumber as e:
            print(e)


def menu() -> None:
    """
    Muestra el menú principal y gestiona la selección de opciones del usuario.

    Esta función limpia la consola, muestra las opciones del menú principal,
    y dirige el flujo del programa basado en la selección del usuario.

    Returns:
        None

    Raises:
        EndProgram: Cuando el usuario selecciona la opción de salir.
        InvalidInputNumber: Cuando el usuario ingresa un número de opción inválido.

    Side Effects:
        - Limpia la consola antes de mostrar el menú.
        - Interactúa con el usuario a través de la consola (input/output).
        - Llama a otras funciones del programa basadas en la selección del usuario.

    Note:
        Esta función depende de la existencia de las siguientes funciones:
        - limpiar_consola()
        - add_task()
        - menu_view_tasks()
    """
    limpiar_consola()
    indice = int(input('Menu: 1.Añadir Tarea | 2.Ver Tareas | 3.Salir \n'))

    if indice == 1:
        add_task()
    elif indice == 2:
        menu_view_tasks()
    elif indice == 3:
        raise EndProgram()
    else:
        raise InvalidInputNumber


def add_task() -> None:
    """
    Gestiona el proceso de añadir una nueva tarea.

    Esta función guía al usuario a través del proceso de creación de una nueva tarea,
    solicitando los detalles necesarios, mostrando un resumen para confirmación,
    y permitiendo modificaciones antes de guardar la tarea.

    Returns:
        None

    Side Effects:
        - Limpia la consola varias veces durante el proceso.
        - Interactúa con el usuario a través de la consola (input/output).
        - Modifica el almacenamiento de tareas (añade una nueva tarea).
        - Puede llamar a otras funciones como menu_update_task().

    Flujo de la función:
        1. Limpia la consola y obtiene la lista actual de tareas.
        2. Solicita al usuario los detalles de la nueva tarea.
        3. Muestra un resumen de la tarea y pide confirmación.
        4. Si se confirma, añade la tarea a la lista y la guarda.
        5. Si se cancela, termina el proceso.
        6. Si se solicita modificación, permite editar la tarea antes de guardar.

    Note:
        Esta función depende de varias funciones auxiliares para obtener
        los detalles de la tarea y manejar el almacenamiento.
    """
    limpiar_consola()
    tasks_list = obtener_tareas()

    task_name = add_task_name()
    description = add_task_description()
    duracion = add_task_duracion()
    importancia = add_task_importancia()

    task = {
        'task_name': task_name,
        'description': description,
        'date_create': date_time(),
        'duracion': duracion,
        'importancia': importancia,
        'completado': add_task_estado()
    }

    while True:
        limpiar_consola()
        task_details(task)
        validar = input('Desea agregar la tarea (y/n) o modificar algun parametro (m)? \n')
        if validar.lower() == 'y':
            # Solo agregar una nueva tarea si estamos creando una nueva
            tasks_list[str(long_tasks(tasks_list))] = task
            guardar_tasks(tasks_list)
            print('Tarea agregada exitosamente!!')
            time.sleep(1)
            break
        elif validar.lower() == 'n':
            print('Cancelando proceso...')
            time.sleep(1)
            break
        elif validar.lower() == 'm':
            new_task = menu_update_task(task)
            task = new_task
        else:
            print('Ingrese un valor valido')


def add_task_name() -> str:
    """
    Solicita al usuario que ingrese el nombre de una tarea.

    Returns:
        str: El nombre de la tarea ingresado por el usuario.

    Side Effects:
        Interactúa con el usuario a través de la consola (input).
    """
    return input('Ingrese la tarea que desea agregar: ')

def add_task_description() -> str:
    """
    Solicita al usuario que ingrese una descripción opcional para una tarea.

    Returns:
        str: La descripción de la tarea ingresada por el usuario. Puede ser una cadena vacía.

    Side Effects:
        Interactúa con el usuario a través de la consola (input).
    """
    return input('Ingrese una descripcion de la tarea (opcional): ')

def add_task_duracion() -> str:
    """
    Solicita al usuario que ingrese la duración opcional de una tarea.

    Returns:
        str: La duración de la tarea ingresada por el usuario. Puede ser una cadena vacía.

    Side Effects:
        Interactúa con el usuario a través de la consola (input).
    """
    return input('Ingrese la duracion de la tarea (opcional): ')

def add_task_importancia() -> str:
    """
    Solicita al usuario que indique si una tarea tiene prioridad.

    Returns:
        str: 'True' si la tarea tiene prioridad, 'False' si no.
              Note que esto retorna un string, no un booleano.

    Side Effects:
        Interactúa con el usuario a través de la consola (input).

    Note:
        La función no valida la entrada del usuario. Se recomienda validar
        y convertir la entrada a un booleano si es necesario.
    """
    return input('La tarea tiene prioridad (True/False)? ')

def date_time() -> str:
    """
    Genera una marca de tiempo actual en formato 'YYYY-MM-DD HH:MM'.

    Returns:
        str: La fecha y hora actual formateada como string.

    Dependencies:
        - datetime.today() de la biblioteca datetime.
    """
    return datetime.today().strftime("%Y-%m-%d %H:%M")

def add_task_estado() -> str:
    """
    Solicita al usuario que indique si una tarea está completada.

    Returns:
        str: 'True' si la tarea está completada, 'False' si no.
              Note que esto retorna un string, no un booleano.

    Side Effects:
        Interactúa con el usuario a través de la consola (input).

    Note:
        La función no valida la entrada del usuario. Se recomienda validar
        y convertir la entrada a un booleano si es necesario.
    """
    return input('La tarea esta completada (True/False)? ')


def long_tasks(tasks: dict) -> int:
    """
    Cuenta el número de tareas en un diccionario de tareas.

    Args:
        tasks (dict): Un diccionario que contiene las tareas.

    Returns:
        int: El número total de tareas en el diccionario.

    Note:
        Esta función asume que cada elemento en el diccionario representa una tarea.
        Si el diccionario contiene elementos que no son tareas, el conteo podría ser inexacto.
    """
    contador = 0
    for tarea in tasks:
        contador += 1
    return contador


def menu_view_tasks() -> None:
    """
    Muestra un menú interactivo para ver y seleccionar tareas existentes.

    Esta función presenta al usuario una lista de todas las tareas registradas,
    permitiéndole seleccionar una tarea específica para ver sus detalles o salir del menú.

    Returns:
        None

    Side Effects:
        - Limpia la consola antes de mostrar el menú.
        - Interactúa con el usuario a través de la consola (input/output).
        - Puede llamar a otras funciones como view_task_details().
        - Se llama a sí misma recursivamente en caso de entradas inválidas o errores.

    Flujo de la función:
        1. Limpia la consola.
        2. Obtiene todas las tareas registradas.
        3. Si no hay tareas, muestra un mensaje y retorna.
        4. Muestra una lista numerada de las tareas existentes.
        5. Solicita al usuario que seleccione una tarea o ingrese 'q' para salir.
        6. Si el usuario ingresa 'q', la función retorna.
        7. Si el número de tarea es válido, llama a view_task_details() con la tarea seleccionada.
        8. Si el número de tarea es inválido, muestra un mensaje de error y se llama a sí misma.

    Raises:
        KeyError: Capturado internamente. Ocurre si se intenta acceder a una tarea que no existe.

    Dependencias:
        - limpiar_consola(): Función para limpiar la pantalla de la consola.
        - obtener_tareas(): Función para obtener el diccionario de todas las tareas.
        - view_task_details(): Función para mostrar los detalles de una tarea específica.
        - time.sleep(): Utilizado para pausar la ejecución brevemente después de mostrar mensajes de error.

    Note:
        - Esta función utiliza recursión para manejar entradas inválidas o errores, lo que podría
          llevar a un desbordamiento de pila si ocurren muchos errores consecutivos.
        - Se asume que las tareas están almacenadas en un diccionario donde las claves son strings
          que representan números y los valores son diccionarios con los detalles de las tareas.
    """
    limpiar_consola()
    tareas = obtener_tareas()  # Obtener todas las tareas

    if len(tareas) == 0:
        print('No hay tareas registradas.\n\n')
        input('Presione Enter para continuar.')
        return

    try:
        # Mostrar las tareas disponibles
        print('Tareas Existentes: \n')
        for key, task in tareas.items():
            print(f'{key}: {task["task_name"]}')

        # Solicitar al usuario que seleccione una tarea
        task_number = input('\nIngrese el número de tarea que desea ver (o ingrese "q" para salir): ')

        if task_number.lower() == 'q':
            return

        # Verificar si el número de tarea ingresado es válido
        if task_number in tareas:
            task_pos = tareas[task_number]  # Obtener la tarea correspondiente
            view_task_details(task_pos, task_number)
        else:
            print(f'La tarea #{task_number} no existe. Por favor, ingrese un número válido.')
            time.sleep(1)
            menu_view_tasks()  # Volver a mostrar el menú de tareas
    except KeyError as e:
        print(f'Error: {str(e)}. La tarea seleccionada no existe.')
        time.sleep(1)
        menu_view_tasks()  # Volver a mostrar el menú en caso de error


def task_details(task: dict) -> None:
    """
    Imprime los detalles de una tarea en un formato legible.

    Esta función toma un diccionario que representa una tarea y muestra
    sus detalles en la consola de manera estructurada y fácil de leer.

    Args:
        task (dict): Un diccionario que contiene los detalles de la tarea.
                     Debe incluir las siguientes claves:
                     - 'task_name': El nombre de la tarea.
                     - 'description': La descripción de la tarea.
                     - 'duracion': La duración estimada de la tarea.
                     - 'importancia': El nivel de importancia de la tarea.
                     - 'completado': El estado de completitud de la tarea.
                     - 'date_create': La fecha de creación de la tarea.

    Returns:
        None

    Side Effects:
        Imprime los detalles de la tarea en la consola estándar.

    Raises:
        KeyError: Si alguna de las claves requeridas no está presente en el diccionario de la tarea.

    Note:
        Esta función asume que todos los valores en el diccionario de la tarea
        son strings o pueden ser convertidos a strings de manera segura.
    """
    print(f'Nombre: \n\t{task["task_name"]}\nDescripcion: \n\t{task["description"]}\nDuracion: \n\t{task["duracion"]}\nImportancia: \n\t{task["importancia"]}\nCompletado: \n\t{task["completado"]}\nFecha de creacion: \n\t{task["date_create"]}\n')

def view_task_details(task: dict, position: int, modify: bool=False) -> None:
    """
    Muestra los detalles de una tarea y permite al usuario interactuar con ella.

    Esta función presenta dos modos de operación basados en el parámetro 'modifi':
    1. Modo de visualización y edición (modifi=False):
       Muestra los detalles de la tarea y ofrece opciones para modificarla, eliminarla o volver al menú anterior.
    2. Modo de confirmación de modificación (modifi=True):
       Actualiza la tarea en el almacenamiento, muestra los detalles actualizados y espera confirmación del usuario.

    Args:
        task (dict): Un diccionario que contiene los detalles de la tarea a mostrar o actualizar.
        position (int): La posición o índice de la tarea en el listado general de tareas.
        modify (bool, opcional): Indica si la función se está llamando después de una modificación.
                                 Por defecto es False.

    Returns:
        None

    Side Effects:
        - Limpia la consola antes de mostrar información.
        - Interactúa con el usuario a través de la consola (input/output).
        - Puede modificar el almacenamiento de tareas (cuando modifi=True).
        - Puede redirigir a otras funciones del programa (menu_update_task, delete_task, menu_view_tasks).

    Flujo de la función:
        Si modifi es False:
        1. Muestra los detalles de la tarea.
        2. Presenta opciones al usuario: modificar, eliminar o volver.
        3. Basado en la elección del usuario, llama a la función correspondiente.
        4. Si la entrada es inválida, se llama a sí misma recursivamente.

        Si modifi es True:
        1. Actualiza la tarea en el almacenamiento.
        2. Muestra los detalles actualizados de la tarea.
        3. Espera confirmación del usuario para continuar.

    Raises:
        ValueError: Implícitamente, si el usuario ingresa un valor no numérico cuando se espera un número.

    Note:
        Esta función depende de varias funciones externas como limpiar_consola(), task_details(),
        menu_update_task(), delete_task(), menu_view_tasks(), obtener_tareas(), y guardar_tasks().
        Asegúrese de que estas funciones estén definidas y accesibles en el ámbito de ejecución.
    """
    if not modify:
        limpiar_consola()
        print(f'Tarea #{position}: \n')
        task_details(task)
        opcion = int(input('\n\n¿Deseas modificar la tarea? 1.Modificar Tarea | 2.Eliminar Tarea | 3.Volver\n'))
        if opcion == 1:
            menu_update_task(task, position)
        elif opcion == 2:
            delete_task(task, position)
        elif opcion == 3:
            menu_view_tasks()
        else:
            print('Ingrese un número válido')
            time.sleep(1)
            view_task_details(task, position)
    elif modify:
        limpiar_consola()
        dict = obtener_tareas()
        dict[str(position)] = task  # Actualizar la tarea modificada en la posición original
        guardar_tasks(dict)
        print(f'Tarea #{position}: \n')
        task_details(task)
        input('Modificación completada. Presione Enter para continuar.')



def menu_update_task(task: dict, position: int=None) -> dict or None:
    """
    Presenta un menú interactivo para actualizar los campos de una tarea.

    Este método muestra un menú que permite al usuario modificar diferentes
    campos de una tarea existente. El usuario puede actualizar el nombre,
    descripción, duración, importancia y estado de la tarea. El método
    continúa en un bucle hasta que el usuario decide salir y guardar los cambios.

    Args:
        task (dict): Un diccionario que representa la tarea a actualizar.
                     Debe contener las claves 'task_name', 'description',
                     'duracion', 'importancia', y 'completado'.
        position (int, opcional): La posición de la tarea en la lista de tareas.
                                  Si se proporciona, se usa para mostrar el
                                  número de la tarea y para guardar la tarea
                                  actualizada en su posición original.

    Returns:
        dict: El diccionario de la tarea actualizado.

    Raises:
        ValueError: Si el usuario ingresa una opción no válida en el menú.

    Note:
        - Este método depende de funciones externas como limpiar_consola(),
          task_details(), add_task_name(), add_task_description(),
          add_task_duracion(), add_task_importancia(), add_task_estado(),
          obtener_tareas(), guardar_tasks(), y view_task_details().
        - El método utiliza un bucle while True y maneja las excepciones
          internamente para proporcionar una experiencia de usuario robusta.
        - Si se proporciona una posición, la tarea actualizada se guarda
          en esa posición en el almacenamiento de tareas.
    """
    while True:
        try:
            limpiar_consola()
            if position is not None:
                print(f'Tarea #{position}: \n')
            task_details(task)

            modificar_campo = int(input('\n\n¿Qué desea actualizar? 1.Nombre | 2.Descripción | 3.Duración | 4.Importancia | 5.Estado | 6. Salir y Guardar \n'))
            if modificar_campo == 1:
                print(f'Valor actual -> Nombre: {task["task_name"]}')
                task['task_name'] = add_task_name()
            elif modificar_campo == 2:
                print(f'Valor actual -> Descripción: {task["description"]}')
                task['description'] = add_task_description()
            elif modificar_campo == 3:
                print(f'Valor actual -> Duración: {task["duracion"]}')
                task['duracion'] = add_task_duracion()
            elif modificar_campo == 4:
                print(f'Valor actual -> Importancia: {task["importancia"]}')
                task['importancia'] = add_task_importancia()
            elif modificar_campo == 5:
                print(f'Valor actual -> Completado: {task["completado"]}')
                task['completado'] = add_task_estado()
            elif modificar_campo == 6:
                print('Saliendo de: Modificar Tarea...')
                time.sleep(1)
                if position is not None:
                    # Aquí actualizamos la tarea existente en su posición original
                    dict = obtener_tareas()
                    dict[str(position)] = task  # Actualizar la tarea en la posición original
                    guardar_tasks(dict)
                    view_task_details(task, position, True)
                return task
            else:
                raise ValueError
        except ValueError as e:
            print('Ingrese un valor válido')
            menu_update_task(task, position)



def delete_task(task_element: dict, pos: int) -> None:
    """
    Elimina una tarea específica y actualiza el diccionario de tareas.

    Esta función muestra los detalles de una tarea específica, solicita confirmación
    para eliminarla, y si se confirma, elimina la tarea del diccionario global de tareas.
    Luego, reindexar las tareas restantes y guarda los cambios.

    Args:
        task_element (dict): Un diccionario que representa la tarea a eliminar.
        pos (int): La posición o índice de la tarea en el diccionario global de tareas.

    Returns:
        None

    Side Effects:
        - Modifica el diccionario global de tareas.
        - Actualiza el archivo JSON de tareas.
        - Limpia la consola y muestra mensajes al usuario.
        - Puede redirigir al menú principal.

    Flujo de la función:
        1. Muestra los detalles de la tarea y solicita confirmación para eliminarla.
        2. Si se confirma, obtiene el diccionario global de tareas.
        3. Elimina la tarea especificada del diccionario.
        4. Reindexar las tareas restantes para mantener índices consecutivos.
        5. Guarda el diccionario actualizado en el archivo JSON.
        6. Si se cancela la eliminación, informa al usuario.
        7. Después de un breve retraso, redirige al menú principal.

    Note:
        Esta función depende de varias funciones externas como limpiar_consola(),
        task_details(), obtener_tareas(), guardar_tasks(), y menu().
    """
    while True:
        limpiar_consola()
        print(f'Tarea #{pos}: \n')
        task_details(task_element)
        confirmacion = input('\n\nSeguro que desea eliminar la tarea (y/n)?\n (La tarea no se podra recuperar)\n')
        if confirmacion.lower() == 'y':
            tasks = obtener_tareas()
            print('\n\n')
            if str(pos) in tasks:
                del tasks[str(pos)]

                new_dict = {}
                contador = 0
                for elemento in tasks:
                    new_dict[str(contador)] = tasks[str(elemento)]
                    contador = contador + 1
                guardar_tasks(new_dict)
                print('Tarea eliminada corectamente!!!')
                break
        elif confirmacion.lower() == 'n':
            print('Cancelando operacion...')
            break
        else:
            print('Ingrese un valor valido')
            time.sleep(1)
    time.sleep(2)
    menu()



def obtener_tareas(archivo: str='tasks.json') -> dict:
    """
    Obtiene las tareas almacenadas en un archivo JSON.

    Args:
        archivo (str, opcional): Nombre del archivo JSON del que se leerán los datos.
                                 Por defecto es 'tasks.json'.

    Returns:
        dict: Un diccionario conteniendo todas las tareas almacenadas en el archivo JSON.

    Raises:
        FileNotFoundError: Si el archivo especificado no existe.
        json.JSONDecodeError: Si el archivo no contiene JSON válido.
    """
    with open(archivo, 'r') as f:
        return json.load(f)


def crear_json_vacio(archivo: str='tasks.json') -> None:
    """
    Crea un archivo JSON vacío o lo sobrescribe si ya existe.

    Args:
        archivo (str, opcional): Nombre del archivo JSON a crear.
                                 Por defecto es 'tasks.json'.

    Returns:
        None

    Side Effects:
        Crea o sobrescribe un archivo en el sistema de archivos.
    """
    with open(archivo, 'w') as f:
        json.dump({}, f)


def guardar_tasks(tasks_list: dict, archivo: str='tasks.json') -> None:
    """
    Guarda un diccionario de tareas en un archivo JSON.

    Args:
        tasks_list (dict): Diccionario conteniendo las tareas a almacenar.
        archivo (str, opcional): Nombre del archivo JSON en el que se guardarán los datos.
                                 Por defecto es 'tasks.json'.

    Returns:
        None

    Side Effects:
        Crea o sobrescribe un archivo en el sistema de archivos.
    """
    with open(archivo, 'w') as f:
        json.dump(tasks_list, f, indent=2)


def limpiar_consola() -> None:
    """
    Limpia la pantalla de la consola en Windows, macOS y Linux.

    Returns:
        None

    Side Effects:
        Limpia la pantalla de la consola del sistema operativo actual.

    Note:
        Esta función usa comandos específicos del sistema operativo y puede
        no funcionar en todos los entornos, especialmente en IDEs o entornos
        de desarrollo integrados.
    """
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS y Linux
        os.system('clear')

if __name__ == '__main__':
    main_menu()