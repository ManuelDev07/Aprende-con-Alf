from io import open
from typing import Dict
from urllib import request
from urllib.error import URLError


#Ejercicio Nro1 - Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.
numero = int(input("Ingrese un número entero entre 1 y 10: "))
nombre = 'Tabla del ' + str(numero) + '.txt'

archivo = open(nombre, 'w')
archivo.write(f"Tabla de Multiplicar del {str(numero)}: \n")

for i in range(1, 11):
    resultado = numero * i
    archivo.write(str(numero) + ' x ' + str(i) + ' = ' + str(numero*i) + '\n')

archivo.close()

#Ejercicio Nro2 - Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
num = int(input("Ingrese un número entero entre 1 y 10: "))
nombre_archivo = 'Tabla del ' + str(num) + '.txt'

try:
    archivo = open(nombre_archivo, 'r')
    print(archivo.read())
    archivo.close()

except FileNotFoundError:
    print("ERROR! No existe un archivo con ese nombre.")

#Ejercicio Nro3 - Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
n = int(input("Ingrese un número entero entre 1 y 10: "))
m = int(input("Ingrese la nro de la línea donde se empezará a leer el documento: "))
nombre_archivo = 'Tabla del ' + str(n) + '.txt'

try:
    archivo = open(nombre_archivo, 'r')
    leer = archivo.readlines()[m]
    print(leer)
    archivo.close()

except FileNotFoundError:
    print("ERROR! No existe un archivo con ese nombre.")

#Ejercicio Nro4 - Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número de palabras que contiene.
print("Saber el Número de Letras que contiene una pagina")
url = input("Ingrese la URL de la pagina: ")

try:
    pagina = request.urlopen(url)
    leer = pagina.read()
    print(f"La página posee {len(leer)} letras.")

except URLError:
    print("ERROR! Esa url no existe :(")

'''
#Ejercicio Nro6 - Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los
clientes de una empresa. El programa incorporar funciones tales como:

-Crear el fichero con el listín si no existe
-Consultar el teléfono de un cliente
-Añadir el teléfono de un nuevo cliente
-Eliminar el teléfono de un cliente

NOTA:El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben 
aparecer separados por comas y cada cliente en una línea distinta.
'''
print("""
Menú
-(Usar 1) Para CREAR un nuevo Listín Telefónico.
-(Usar 2) Para AÑADIR el teléfono de un cliente.
-(Usar 3) Para CONSULTAR el teléfono de un nuevo cliente.
-(Usar 4) Para ELIMINAR el teléfono de un cliente.
-(Usar 5) Para SALIR del programa.
""")

def crear_archivo():
    try:
        archivo = open('listin.txt', 'w')

    except FileExistsError:
        print("ERROR! Ya existe un archivo telefónico.")

    else:
        print(f"El Archivo {archivo.name} ha sido creado con éxito. ")
        archivo.close()


def consultar_cliente(nombre):
    try:
        archivo = open('listin.txt', 'r')
    except FileNotFoundError:
        print("ERROR! Archivo no encontrado o no existe!.")
    else:
        consulta = archivo.readlines()
        archivo.close()
        consulta = dict([tuple(linea.split(',')) for linea in consulta])

        if nombre in consulta:
            return consulta[nombre] 

        else:
            print(f"El cliente {nombre} no existe!.")
        
            

def agregar_cliente(nombre, numero):
    try:
        archivo = open('listin.txt', 'a')
        
    except FileNotFoundError:
        print("ERROR! Archivo no encontrado o no existe!.")
    
    else:
        archivo.write(f"Nombre: {nombre}, Telefono: {numero}\n")
        archivo.close()
        return "Cliente agendado con éxito."

def eliminar_cliente(nombre):
    try:
        archivo = open('listin.txt', 'r')

    except FileNotFoundError:
        print("ERROR! Archivo no encontrado o no existe!.")
    
    else:
        consulta = archivo.readlines()
        archivo.close()
        consulta = dict([tuple(linea.split(', ')) for linea in consulta])

        if nombre in consulta:
            del consulta[nombre]
            f = open('listin.txt', 'w')
            
            for nombre, telf in consulta.items():
                f.write(nombre + ',' + telf)
            f.close()
            return ('¡El cliente se ha borrado!\n')
        
        else:
            return("El Cliente no existe. D:")

while True:
    try:
        opcion = int(input("\nEsperando una opción: "))

    except ValueError:
        print("ERROR! Debe ingresar el dato como se le indica.")


    if opcion == 1:
        crear_archivo()

    elif opcion == 3:
        nombre = input("\nIngrese el nombre del cliente que desea consultar: ")
        print(consultar_cliente(nombre))
        
    elif opcion == 2:
        dict = {}
        print("\nIngrese los datos del cliente (Su Nombre y Número de Teléfono)")
        nombre = input("Ingrese el nombre del cliente: ")
        numero = input("Ingrese el número de teléfono del cliente: ")
        print(agregar_cliente(nombre, numero))

    elif opcion == 4:
        nombre = input("\nIngrese el nombre del cliente que desea eliminar: ")
        print(eliminar_cliente(nombre))
        
    elif opcion == 5:
        print("Hasta Pronto.")
        break
    else:
        print("Opción inexistente... Intente de nuevo.")