'''
/*
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
'''

#Asignación de variables por valor

my_num1 = 90
my_num2 = 30
print(f"{my_num1}, {my_num2}")

#Cambiamos el valor de la variable
my_num2 = 10

#La posición en memoria de my_num1 y my_num2, aunque se asigne el valor de otra variable, tiene su propia referencia en memoria (posición)
my_num1 = my_num2
print(f"{my_num1}, {my_num2}")

#Asignación de valores por referencia

my_set1 = set()

my_set1 = {"David",34}
my_set2 = {"Noelia",32}

#my_set1 apunta a la dirección de memoria de my_set2, creando una Referencia de ella, estan guardado en la misma posición de memoria
my_set1 = my_set2
print(my_set1)

'''
Agregamos elemento, al ser una referencia, modificando set1 modificamos también en consecuencia el set2
my_set1 también agrega "test" en consecuancia a los dos set, ya que tienen el mismo contenido, pues es una referencia
'''
my_set2.add("test")
print(my_set1)
print(my_set2)

#Funciones con datos por valor

my_int = 34

def values(my_int_param: int):
    #Reasignamos e imprimimos
    my_int_param = 32
    print(my_int_param)
    
values(my_int)

#Funciones con datos por referencia

def references(my_list_param: list):
    # ¡OJO! Estamos trabajando con referencias, la lista dada como parámetro también será modificada!
    #Agregamos tanto al parámetro como a la variable por referencia, ya que toma referencia de la variable pasada por parámetro, en este caso una lista
    my_list_param.append(30)
    print(my_list_param)
    
my_list1 = [50,40]

references(my_list1)
#Al ser referencia, la funcion modifica también la lista enviada
print(my_list1)

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
 */
'''

def func_references(ref_var1: list, ref_var2: list):
    ref_var1.append(20)
    ref_var2 = ref_var1
    ref_var2.append(100)
    return ref_var1,ref_var2        #La referencia toma el valor del mismo sitio! Son punteros

def func_values(value1: int, value2: int):
    temp = value1   #temp = 10
    value1 = value2 #value2 = 20
    value2 = temp   #value1 = 10
    return value1,value2

my_int1 = 10
my_int2 = 20
result_value1, result_value2 = func_values(my_int1,my_int2)
print(f"{my_int1} {my_int2}")
print(f"{result_value1} {result_value2}")

my_list_1 = [10,20]
my_list_2 = [30,80]
ref_value1, ref_value2 = func_references(my_list_1,my_list_2)
print(f"{my_list_1} {my_list_2}")
print(f"{ref_value1} {ref_value2}")

if(ref_value1 == ref_value2):
    print("Efectivamente, al ser referencias una de otra toman el mismo valor, actúan como punteros")
else:
    print("Oh, no!!")