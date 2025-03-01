'''
NOTA:
Una estructura de datos es una forma de organizar, gestionar y almacenar
datos para que se puedan acceder y trabajar con ellos de manera eficiente.
En Python, hay varias estructuras de datos integradas que son fundamentales
para la programación y el manejo de datos.
'''

'''
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
'''
my_list = [3,7,5,9]

my_list.sort()  #Orenación
print(my_list)
print(f"Se ha eliminado el valor {my_list.pop()} de la lista")   #Eliminar último elemento de la lista
print(my_list)
my_list[0]=101  #Actualización del valor en la posición 0 de la lista
print(my_list)
my_list.append(9999)    #Inserción
print(my_list)
my_list.remove(9999)    #Eliminación de un elemnto de la lista
print(my_list)

my_tuple = (10,22,41,9,10)
#Las tuplas son inmutables
print(my_tuple[1])  #Acceso, posición 1 de la tupla (22)
print(my_tuple.count(10))   #Cuantas veces aparece el valor 10
print(my_tuple.index(9))   #¿Dónde esta el primer valor 9?
#Podemos ordenar, pero devuelve una lista. Convertir después a tupla
my_tuple = tuple(sorted(my_tuple)) #Todos los valores deben ser del mismo tipo primitivo
print(my_tuple)

my_set = {91,32,11,101}
print(my_set)
#Los set's no se pueden ordenar, a menos que usemos listas
my_set.add(98)  #Inserción
print(my_set)
my_set.remove(98)   #Eliminación
print(my_set)
#Los set's no permiten asignación

my_dict = {"name":"david","surname":"valls"}
#No podemos acceder a la posición X ya que trabajamos con clave-valor
print(my_dict["name"])  #Accedenis al valor de la clave name
my_dict["name"] = "Brais"   #Actualización del valor en la clave name
my_dict["country"] = "Valencia"  #Agregamos la clave country con el valor Valencia
print(my_dict)
del my_dict["country"]      #Eliminamos la clave country, ¡No todo el diccionario!
print(my_dict)
my_dict = dict(sorted(my_dict.items()))   #Ordenación de los items del diccionario
print(my_dict)
 
'''
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
'''
list_contacts = {}

def search_contact(name):
    if name in list_contacts:
        print(f"El contacto {name} tiene el teléfono {list_contacts[name]}")
    else:
        print("El contacto no existe")

def insert_contact(name, phone):
    list_contacts[name] = phone
    print(f"Se ha agregado el contacto {name} con el teléfono {phone}")
    
def refresh_contact(name,phone):
    if name in list_contacts:
        list_contacts[name] = phone
    else:
        print("El contacto no existe")

def remove_contact(name):
    if name in list_contacts:
        del list_contacts[name]
    else:
        print("El contacto no existe")
        
def show_contacts():
    for contact in list_contacts.items():
        print(f"Nombre: {contact[0]}")
        print(f"Teléfono: {contact[1]}")
    
exit = False
while not exit:
    print("----------------------------")
    print("1. Agregar contacto")
    print("2. Actualizar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Ver contactos")
    print("ANY_KEY: Salir")
    print("----------------------------")
    option = input("Ingrese una opción: ")
    print("----------------------------")
    
    match option:
        case "1":
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            try:
                if len(phone) >= 11 or len(phone) <= 0:
                    print("Error!")
                else:
                    insert_contact(name, phone)
            except Exception as error:
                print(f"No se pudo realizar la operación: {error}")
        case "2":
            name = input("Nombre: ")
            phone = input("Teléfono: ")
            try:
                if len(phone) >= 11 or len(phone) <= 0:
                    print("Error!")
                else:
                    refresh_contact(name, phone)
            except Exception as error:
                print(f"No se pudo realizar la operación: {error}")
        case "3":
            name = input("Nombre: ")
            try:
                search_contact(name)
            except Exception as error:
                print(f"No se pudo realizar la operación: {error}")
        case "4":
            name = input("Nombre: ")
            try:
                remove_contact(name)
            except Exception as error:
                print(f"No se pudo realizar la operación: {error}")
        case "5":
            show_contacts()
        case _:
            exit = True