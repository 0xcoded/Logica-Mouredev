'''
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 '''

string1 = "Hola"
string2 = "Python"

#Concatenación
string3 = string1 + " " + string2
print(string3)

#indexación
print(string3[0])

#Repetición
print((string3 + " ") * 4)

#Logintud
print(len(string3))

#Slicing
print(string3[0:4])
print(string3[:4])
print(string3[4:])
print(string3[2:-2])

#Búsqueda
print("la" in string3)

#Reemplazo
string3 = string3.replace("ola","OLA")
print(string3)

#División de cadenas
list1 = string3.split(" ")
print(list1)

#Mayus, minus
print(string3.lower())
print(string3.upper())

#Primera letra en mayusculas, o cada una
string3 = string3.capitalize()
print(string3)
string3 = string3.title()
print(string3)

#Eliminar primer y último espacio
string3 = " Hola Python "
string3 = string3.strip()
print(string3)

#Búsqueda inicio - final
print(string3.startswith("Hola"))
print(string3.endswith("Python"))

#Búsqueda de posición
print(string3.find("la"))

#Búsqueda ocurrencias
print(string3.lower().count("o"))

#Formateo de cadenas
name = "David"
surname = "valls"
print("Hola {} {}".format(name,surname))

#Interpolación de cadenas
print(f"Hola {name} {surname}")

#Cadena a lista
list1 = list(string3)
print(list1)

#Lista a cadena
string3 = ""
string3 = string3.join(list1)
print(string3)

#Transformación numérica
string1 = "123123"
int1 = int(string1)
float1 = float(string1)
print(int1)
print(float1)

#Comprobación numérica
print(string1.isnumeric())
print(string1.isdigit())
print(string1.isalnum())
print(string1.isalpha())

'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
'''

#Palíndromo
def check_palindrome(word1):
    if word1 == word1[::-1]:
        print(f"{word1} es Palíndromo")
    else:   
        print("No es un palíndromo")
    
#Anagrama
def check_anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        print(f"{word1} es anagrama de {word2}")
    else:
        print("No son anagramas")
    
#Isograma
def check_isogram(word1):
    if len(word1) == len(set(word1)):
        print(f"{word1} es isograma")
    else:
        print(f"{word1} no es isograma")
    
check_palindrome("radar")
check_anagram("roma","amor")
check_isogram("david")
check_isogram("python")