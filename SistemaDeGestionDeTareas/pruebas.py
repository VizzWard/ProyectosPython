import json
from datetime import datetime

# Variables globales
tasks = {}

def obtener_tareas():
    with open('tasks.json', 'r') as f:
        return json.load(f)

def guardar_tasks(dict):
    """
        Guarda los datos en un archivo JSON.
    """
    with open('tasks.json', 'w') as f:
        json.dump(dict, f, indent=2)

def long_tasks(dict):
    contador = 0
    for tarea in dict:
        contador += 1
    return contador

def add_task(dict):
    """
    Los atributos de las tareas deben contener:
        - nombre de la tarea
        - nota/descripcion
        - fecha de creacion
        - fecha para realizar la tarea
        - duracion
        - importancia/prioridad (True/False)
        - completado (True/False)
    """
    task_name = input('Ingrese la tarea que desea adicionar: ')
    description = input('Ingrese una descripcion de la tarea (opcional): ')
    duracion = input('Ingrese la duracion de la tarea (opcional): ')
    importancia = input('La tarea tiene prioridad?: ')

    task = {
        'task_name' : task_name,
        'description' : description,
        'date_create' : date_time(),
        'duracion' : duracion,
        'importancia' : importancia,
        'completado' : False
    }

    print(task)
    dict[ int(long_tasks(dict)) ] = task
    guardar_tasks(dict)
    tasks = obtener_tareas()

def date_time():
    return datetime.today().strftime("%Y-%m-%d %H:%M")

tasks = obtener_tareas()

for tarea in tasks:
    print(tarea, tasks[tarea]['task_name'])