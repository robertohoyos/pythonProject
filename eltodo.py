import argparse #esta librería está interesante para cosas de línea de comando

# agrega una tarea, abriendo archivo y agregando una línea (con su break)
def add_task(args):
    with open('todo.txt', 'a') as f:    #abre el file aunque no exista
        f.write(args.task + '\n')   # el breakline es importante
    print(f'Added task "{args.task}"')

#es el proceso inverso, remueve la línea, pero no la marca como completada
def remove_task(args):
    with open('todo.txt', 'r') as f:
        tasks = f.read().splitlines() #abre el archivo rompiendo las líneas y todo lo pone separado en una variable
    if args.task_number < 1 or args.task_number > len(tasks): #manejo de excepciones antes de operar
        print(f'Invalid task number: {args.task_number}')
        return
    removed_task = tasks.pop(args.task_number - 1) #el pop es un método también sencillo
    with open('todo.txt', 'w') as f:
        f.write('\n'.join(tasks))   #abre el archivo y por qué de una nueva línea le une nuevamente (sobre escribe)
    print(f'Removed task "{removed_task}"')

def list_tasks(args):
    with open('todo.txt', 'r') as f:
        tasks = f.read().splitlines()
    if not tasks:
        print('No tasks')
        return
    for i, task in enumerate(tasks, 1): # la numeración está al presentarse, pero no en el archivo
        if not args.hide_done or not task.startswith('[x]'):
            print(f'{i}. {task}')

# dónde está recibiendo el argumento del número?
def complete_task(args):
    with open('todo.txt', 'r') as f:
        tasks = f.read().splitlines()
    if args.task_number < 1 or args.task_number > len(tasks):
        print(f'Invalid task number: {args.task_number}')
        return
    completed_task = tasks[args.task_number - 1]
    tasks[args.task_number - 1] = f'[x] {completed_task}' # simplemente le agrega una equis de que está completado, pero no lo manda al completed
    with open('todo.txt', 'w') as f:
        f.write('\n'.join(tasks))   # quizá este join se pueda optimizar, veo que se repite
    print(f'Completed task "{completed_task}"')

parser = argparse.ArgumentParser(description='A command-line todo.txt application')
subparsers = parser.add_subparsers()

add_parser = subparsers.add_parser('add', help='Add a task')
add_parser.add_argument('task', help='The task to add')
add_parser.set_defaults(func=add_task)

remove_parser = subparsers.add_parser('remove', help='Remove a task')
remove_parser.add_argument('task_number', type=int, help='The number of the task to remove')
remove_parser.set_defaults(func=remove_task)

complete_parser = subparsers.add_parser('complete', help='Complete a task') # es con un número?
complete_parser.add_argument('task_number', type=int, help='The number of the task to complete')
complete_parser.set_defaults(func=complete_task)

list_parser = subparsers.add_parser('list', help='List all tasks')
# notar que esto es un nuevo argumento de la función, como opción
list_parser.add_argument('--hide-done', action='store_true', help='Hide completed tasks') # nueva línea
list_parser.set_defaults(func=list_tasks)


args = parser.parse_args()
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()


# todos: interntar agregar la fecha en el formato de todo para cada item cuando se inserte
# todo: cuando se complete una tarea también agregar la fecha en que se completó
# agregar una excepción que ya no se muestre en la lista}



# DONE
# agregado un método que complete las tareas (de momento no ponerlo en un nuevo file)
