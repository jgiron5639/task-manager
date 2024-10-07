import json
import os

#Archivo donde se guardan las tareas
TASKS_FILE = 'tasks.json'

#Función para cargar las tareas desde el archivo JSON
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

#Función para guardar las tareas en el archivo JSON
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

#Función para agregar una nueva tarea
def add_tasks():
    title = input("Ingrese el título de la tarea: ")
    priority = input("Ingrese la prioridad (alta, media, baja): ").lower()

    if priority not in ['alta', 'media', 'baja']:
        print("Prioridad no válida. Intente de nuevo.")
        return

    tasks = load_tasks()
    tasks.append({
        'title': title,
        'priority': priority,
        'completed': False
    })
    save_tasks(tasks)
    print(f"Tarea '{title}' añadida con prioridad {priority}.")

#Función para mostrar todas las tareas
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas.")
        return

    print("\n=== Lista de Tareas ===")
    for i, task in enumerate(tasks, start=1):
        status = "Completada" if task['completed'] else "Pendiente"
        print(f"{i}. {task['title']} (Prioridad: {task['priority']}, Estado: {status})")
    print()

#Función para marcar una tarea como completada
def complete_task():
    list_tasks()
    tasks = load_tasks()
    try:
        task_index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Tarea '{tasks[task_index]['title']}' marcada como completada.")
    except (IndexError, ValueError):
        print("Número de tarea inválido.")

#Función para eliminar una tarea
def delete_task():
    list_tasks()
    tasks = load_tasks()
    try:
        task_index = int(input("Ingrese el número de la tarea a eliminar: ")) -1
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Tarea '{removed_task['title']}' eliminada.")
    except (IndexError, ValueError):
        print("Número de tarea inválido.")

#Función principal para mostrar el menú de opciones
def main_menu():
    while True:
        print("\n=== Gestor de Tareas ===")
        print("1. Añadir nueva tarea")
        print("2. Listar todas las tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        choice = input("Seleccione una opción (1-5): ")

        if choice == '1':
            add_tasks()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no válida. Intente de nuevo")

if __name__ == "__main__":
    main_menu()