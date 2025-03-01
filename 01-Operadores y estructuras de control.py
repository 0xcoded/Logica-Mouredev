'''
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
#Operadores aritméticos
print(3+2)
print(7-2)
print(8/4)
print(10*2)
print(2**8)
print(50//7)
print(104%2)

#Operadores lógicos
print(3+2==5 and 4+1==5)    #Ambos son iguales
print(3+2==5 or 4+4==5)     #Al menos se cumple una igualdad
print(not 3+2 == 5)         #Invertimos la comparacion (not true == false)

#Operadores de comparación
print(3==3)
print(3!=3)

#Operadores de asignación
my_number = 10
my_number += 2
print(my_number)

#Operadores de identidad
name = "David"
name2 = "David"
print(name is name2)        #¿El contenido en memoria de ambas direcciones son iguales?
print(name is not name2)    #¿No son iguales? (not)

#Operadores de pertenencia
print("Dav" in name)        #"Dav" está en "David"
print("Dav" not in name)    #"Dav" no está en "David"

#Operadores de bit's
num1 = 4    #0100
num2 = 7    #0111
'''
AND:
0 0 = 0
1 1 = 1
0 1 = 0
0 1 = 0
0100 = int(4)
'''
print(num1 & num2) # => AND => 0100  => int(4)
''' 
OR: Si almenos un bit vale 1, el resultado vale 1
0 0 = 0
1 1 = 1
0 1 = 1
0 1 = 1
0111 = int(7)
'''
print(num1 | num2)  # OR
'''
XOR: Si los bits son distintos, vale 1, si son iguales, 0
0 0 = 0
1 1 = 0
0 1 = 1
0 1 = 1
0011 = int(3)
'''
print(num1 ^ num2)  # XOR
'''NOT: Invertir valor bit a bit
0 = 1
1 = 0
0 = 1
0 = 1
1011 = 11
'''
print(~num1)
'''Desplazamiento: Mover bits hacia la derecha o izquierda
4 >> 2
0100 => 0001
int(1) 

4 << 2
0100 => 1 0000 = int(16)
'''
print(num1 << 2)

#Estructuras de control

#Condicionales:
if num1 == num2:
    print("Los números son iguales")
elif num1 > num2:
    print("Es mayor")
else:
    print("Son diferentes y no es mayor")
    
#Iterativas:
list_numbers = [10,3,12,4]
for number in list_numbers:
    print(number)
    
for i in range(0,11):
    print(i)
    
j = 0

while j<=10:
    print(j)
    j += 1
    
#while True (Bucle infinito, romper con break)

#Excepciones
try:
    print(10/0)
except Exception as error:
    print(f"ERROR: {error}")
else:
    print("No hay excepciones!")
finally:
    print("Fin del control de errores")
    
'''
* DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, 
 y que no son ni el 16 ni múltiplos de 3.
 '''
for i in range(10,56,2):
     if not i % 16 == 0 and not i % 3 == 0:
         print(i)