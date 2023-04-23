# Roberto Hoyos, 23 Abril 2023
# Mi pŕimer todo.txt en python, simple

# es más rápido usar un alias de bash para manipulare el file

import argparse #esta librería está interesante para cosas de línea de comando
import datetime
import re # para expresiones

# agrega una tarea, abriendo archivo y agregando una línea (con su break)
def add_task(args):
    # get current date and time
    current_time = datetime.datetime.now()
    date_prefix = current_time.strftime("%Y-%m-%d") # format date as YYYY-MM-DD
    with open('todo.txt', 'a') as f:    #abre el file aunque no exista
        f.write(date_prefix + ' ' + args.task + '\n')   # el breakline es importante
    print(f'Added task "{args.task}"')
# lo hace directo en el archivo, sería bueno tenerlo como variable y luego imprimirlo en el archivo

#es el proceso inverso, remueve la línea, pero no la marca como completada
# este método puede ser utilizado para el file de los completed
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
        if not args.hide_done or not task.startswith('[x]'): # no imprime la línea en una de estas condiciones
            if args.hide_date: # para ocultar la fecha cuando imprimimos
                linea_en_pedacitos = task.split(" ", 1)
                print(f'{i}. {linea_en_pedacitos[1]}')
            elif args.busca:
                if check_comma_separated_string(task, args.expresion):
                    print(f'{i}. {task}')
                elif check_underscore_separated_string(task, args.expresion):
                    print(f'{i}. {task}')
            else:
                print(f'{i}. {task}')


# este método es para que busque cualquiera de los terminos
def check_comma_separated_string(big_string, regex_string):
    pattern = '|'.join(regex_string.split(','))
    return bool(re.search(pattern, big_string))

def check_underscore_separated_string(big_string, regex_string):
    pattern = '.*'.join(regex_string.split('_'))
    return bool(re.search(pattern, big_string))


# dónde está recibiendo el argumento del número?
# agregar aquí la fecha cuando se complete la tarea
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
list_parser.add_argument('--hide-date', action='store_true', help='Hide dates of the tasks') # nueva línea, default value false store_true para la opción
list_parser.add_argument('--busca', action='store_true', help='list only items with the arguments') # nueva línea
list_parser.add_argument('--expresion', help='The expression to search for')
list_parser.set_defaults(func=list_tasks)


args = parser.parse_args()
if hasattr(args, 'func'):
    args.func(args)
else:
    parser.print_help()



# todo: cuando se complete una tarea también agregar la fecha en que se completó
# con calma ver los colorcitos que se le pueden poner a la línea de comando
# la prioridad se asigna antes de la fecha, es decir, una condición cuando vaya ingresar una prioridad que lo coloque antes de la fecha
# poner otra reglita que el due se pueda poner tomorrow today, next week (para más fácil)
# poner una suerte de contador para que confirme si encontró o no
# una tarea que sólo me de los tags

# DONE
# agregado un método que complete las tareas (de momento no ponerlo en un nuevo file)
# todos: interntar agregar la fecha en el formato de todo para cada item cuando se inserte
# opción de ocultar la fecha de creación de las tareas
# mostrar todas las líneas que tengan el texto de una persona
# probar también con expresiones regulares, tanto para or como para and