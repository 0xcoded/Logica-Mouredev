'''
* EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
'''
def countdown(num):
    if num >= 0:            #Si no hay comprobación de cuando finalizar la función recursiva, nunca dejaría de ejecutarse (-1,-2,-3...)
        print(num)
        countdown(num-1)    #Se llama a si misma pero con un nuevo parámetro, que equivale a num - 1, se llama con un número menos
        
countdown(100)

'''
* DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 '''


def factorial(num):
    if num == 0:
        return 1
    if num < 1:
        return 0
    return num * factorial(num-1)   # 5 * 4, llama con 4, 4 * 3...

def fibonacci(num):
    if num <= 0:
        return 0
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)  #(pos-1) + (pos-2)

print(factorial(5))
print(factorial(0))
print(factorial(-5))

print(fibonacci(8))        #18 -> pos-1 (8) + post-2 (5)    #13
print(fibonacci(13))                                        #144

'''
EXTRA David -> Mostrar sucesión de Fibonacci hasta una posición utilizando la funcion recursiva anterior
'''

#Mostrar los 16 primeros resultados de la fórmula de fibonacci
def list_fibonacci(num):
    for i in range(3,num+1):
        print(fibonacci(i))
        
list_fibonacci(16)

