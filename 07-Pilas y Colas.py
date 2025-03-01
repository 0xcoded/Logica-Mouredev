'''
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
'''

# Pila

def push(*items, stack: list):
    for item in items:
        stack.append(item)
        print(f"Apilando {item} ( {stack} )")
        
def pop(stack: list):
    print(f"Desapilando {stack[len(stack) - 1]}")
    del stack[len(stack) - 1]               #LIFO, Eliminamos el ultimo elemento en entrar
    print(f"Resultado: {stack}")
    
stack = []

push("1","2","3",stack=stack)

pop(stack)
pop(stack)

push("david",stack=stack)
pop(stack)

# Cola

def dequeue(stack: list):
    removed_item = stack.pop(0)    #FIFO, Eliminamos el primer elemento en entrar
    print(f"Se ha eliminado {removed_item} de la cola")
    print(f"Cola: {stack}")
    
stack = []
push("david","noelia","brais",stack=stack)
dequeue(stack)

'''
* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
'''

def back_navigation(stack: list):
    stack.pop()
    

def forward_navigation(full_history: list,stack: list):
    next_page = full_history[len(stack)]
    add_url_navigation(stack,next_page)

def add_url_navigation(stack: list,url: str):
    stack.append(url)
    print(stack)

def navigator():
    stack_navigator = []
    full_history = []

    while True:
        action = input("atras/adelante/salir/historial o URL: ")
        if action == "atras":
            if len(stack_navigator) > 0:
                back_navigation(stack_navigator)
        
        elif action == "adelante":
            if len(full_history) > 0:
                forward_navigation(full_history,stack_navigator)
            else:
                print("Historial vacío.")
        
        elif action == "salir":
            break
    
        elif action == "historial":
            if len(full_history) > 0:
                print(f"Historial: {full_history}")
            else:
                print("Historial vacío.")
    
        else:   #URL
            add_url_navigation(stack_navigator,action)
            full_history = stack_navigator.copy()
        
        if len(stack_navigator) > 0:
            print(f"Estás en la URL: {stack_navigator[len(stack_navigator) - 1]}")
        else:
            print("Página de inicio")
            
#navigator()

def printer():
    queue = []
    
    while True:
        action = input("salir/imprimir o ingrese un nuevo documento: ")
    
        if action == "salir":
            print("Saliendo...")
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo {queue[0]}")
                queue.pop(0) 
            else:
                print("Cola de impresión vacía.")               
        else:
            queue.append(action)
        
        print(f"Cola de impresión: {queue}")
        
printer()