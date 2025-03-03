'''
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
'''

class Animal:
    race = "Breton"
    def __init__(self,name,age,type):
        self.name = name
        self.age = age
        self.type = type
    
    def animal_talk(self):
        print(f"{self.name} tiene {self.age} años y es un {self.type} de la raza {self.race}")
            

simba = Animal("Simba",11,"perro")
simba.animal_talk()
simba.race = "pitbull"
simba.animal_talk()
simba.name = "Simbull"
simba.age = 7
simba.type = "gato"
simba.race = "pastor alemán"
simba.animal_talk()

'''
* DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 */
 '''
 
class Stack:
    def __init__(self,stack: list):
        self.stack = stack
    #LIFO
    def push(self, item):
        self.stack.append(item)
        print(f"Añadido a la pila: {item}")
        
    def pop(self):
        removed_item = self.stack.pop(len(self.stack) - 1)
        print(f"Eliminado de la pila: {removed_item}")
        
    def count(self):
        return len(self.stack)
    
    def print(self):
        return self.stack
     
class Queue:
    def __init__(self,stack: list):
        self.stack = stack
    #FIFO
    def push(self, item):
        self.stack.append(item)
        print(f"Añadido a la cola: {item}")
        
    def pop(self):
        removed_item = self.stack.pop(0)
        print(f"Eliminado de la cola: {removed_item}")
        
    def count(self):
        return len(self.stack)
    
    def print(self):
        return self.stack
    
my_stack = []
my_stack2 = Stack(my_stack)
my_stack2.push("Elemento 1")
my_stack2.push("Elemento 2")
my_stack2.push("Elemento 3")
print(f"Stack actual: {my_stack2.print()}")
my_stack2.pop()
print(f"Longitud del stack: {my_stack2.count()}")
print(f"Stack actual: {my_stack2.print()}")

my_queue = []
my_queue2 = Queue(my_queue)
my_queue2.push("Elemento 1")
my_queue2.push("Elemento 2")
my_queue2.push("Elemento 3")
print(f"Cola actual: {my_queue2.print()}")
my_queue2.pop()
print(f"Longitud de la cola: {my_queue2.count()}")
print(f"Cola actual: {my_queue2.print()}")