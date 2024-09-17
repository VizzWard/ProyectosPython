import json
import os
import time

from exceptions import EndProgram, InvalidInputNumber, EndMenu
from datetime import datetime

def main_menu():
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


def menu():
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


def add_task():
    limpiar_consola()
    dict = obtener_tareas()

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
            dict[str(long_tasks(dict))] = task
            guardar_tasks(dict)
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


def add_task_name():
    return input('Ingrese la tarea que desea agregar: ')

def add_task_description():
    return input('Ingrese una descripcion de la tarea (opcional): ')

def add_task_duracion():
    return input('Ingrese la duracion de la tarea (opcional): ')

def add_task_importancia():
    return input('La tarea tiene prioridad (True/False)? ')

def date_time():
    return datetime.today().strftime("%Y-%m-%d %H:%M")

def add_task_estado():
    return input('La tarea esta completada (True/False)? ')


def long_tasks(list):
    contador = 0
    for tarea in list:
        contador += 1
    return contador


def menu_view_tasks():
    limpiar_consola()
    tareas = obtener_tareas()  # Obtener todas las tareas

    if len(tareas) == 0:
        print('No hay tareas registradas.')
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


def view_tasks(dict):
    if not dict :
        print('No hay tareas agregadas!!')
    else:
        for task in dict:
            print(f'Tarea #{task} -> {dict[task]['task_name']:<15}Completado: {dict[task]['completado']}')


def task_details(dict):
    print(f'Nombre: \n\t{dict["task_name"]}\nDescripcion: \n\t{dict["description"]}\nDuracion: \n\t{dict["duracion"]}\nImportancia: \n\t{dict["importancia"]}\nCompletado: \n\t{dict["completado"]}\nFecha de creacion: \n\t{dict["date_create"]}\n')

def view_task_details(task, position, modifi=False):
    if not modifi:
        limpiar_consola()
        print(f'Tarea #{position}: \n')
        task_details(task)
        opcion = int(input('\n\n¿Deseas modificar la tarea? 1.Modificar Tarea | 2.Eliminar Tarea | 3.Volver\n'))
        if opcion == 1:
            menu_update_task(task, position)
        elif opcion == 2:
            delete_task()
        elif opcion == 3:
            menu_view_tasks()
        else:
            print('Ingrese un número válido')
            time.sleep(1)
            view_task_details(task, position)
    elif modifi:
        limpiar_consola()
        dict = obtener_tareas()
        dict[str(position)] = task  # Actualizar la tarea modificada en la posición original
        guardar_tasks(dict)
        print(f'Tarea #{position}: \n')
        task_details(task)
        input('Modificación completada. Presione Enter para continuar.')



def menu_update_task(task, position=None):
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



def delete_task():
    print('proximamente')
    time.sleep(2)
    menu()



def obtener_tareas():
    with open('tasks.json', 'r') as f:
        return json.load(f)


def crear_json_vacio():
    """
    Crea un archivo JSON vacío. Si el archivo ya existe, lo sobrescribe con un objeto vacío.
    """
    with open('tasks.json', 'w') as f:
        json.dump({}, f)


def guardar_tasks(dict):
    """
        Guarda los datos en un archivo JSON.
    """
    with open('tasks.json', 'w') as f:
        json.dump(dict, f, indent=2)


def vaciar_json():
    with open('tasks.json', 'w') as f:
        json.dump({}, f)

def limpiar_consola():
    """Limpia la consola en Windows, macOS y Linux."""
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para macOS y Linux
        os.system('clear')


main_menu()