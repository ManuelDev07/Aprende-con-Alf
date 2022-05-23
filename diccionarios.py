#Ejercicio Nro1 - Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
datos = {"Euro":"€", "Dolar":'$', "Yen":"¥"}
while True:
    divisa = input("Ingrese una divisa para ver su símbolo: ").capitalize()
    
    if divisa in datos:
        print(f"Es símbolo del {divisa} es: {datos[divisa]} ")
        break
    else:
        print("ERROR! No existe esa divisa.")

#Ejercicio Nro2 y Nro6 -Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
agenda = {}

def agendar(nombre, edad, direccion, tlf):
    agenda["Nombre"] = nombre
    agenda["Edad"] = edad
    agenda["Dirección"] = direccion
    agenda["Teléfono"] = tlf

    return f"{nombre} tiene {edad} años, vive en {direccion} y su número de teléfono es {tlf}"

while True: #Este bucle while se realizó para la resolución del Ejercicio 6.
    plus = input('\n¿Desea Registrar a una persona a tu agenda? S/N: ')    
    
    if plus.upper() == 'S':
        nombre = input("\nRegistrar Nombre: ")
        edad = int(input("Registrar edad: "))
        direccion = input("Dirección de la persona: ")
        tlf = input("Número de Teléfono: ")

        print(agendar(nombre,edad,direccion,tlf))
    
    else: 
        print("Agenda Cerrada.")
        break


#Ejercicio Nro3 - Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
frutas = {"Plátano":1.35, "Manzana":0.80, "Pera":0.85, "Naranja":0.70}
print("Lista de Precios:")
for fruta in frutas.items():
    print(fruta)

f = input("\nIngrese la fruta que desea comprar: ").title()
peso = float(input("Ingrese el nro de kilos que va a llevar: "))
print(f"El PRECIO TOTAL a PAGAR es de: {frutas[f] * peso:.2f}$")

#Ejercicio Nro4 - Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
calendario = {"1":"Enero", "2":"Febrero", "3":"Marzo", "4":"Abril", "5":"Mayo", "6":"Junio", "7":"Julio", "8":"Agosto", "9":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}
print("Ingrese una fecha en formato dd/mm/aaaa")
dd = int(input("\nIngrese el Día: "))
mm = input("Ingrese el Nro del mes: ")
aaaa = input("Ingrese el Año: ")

print(f"{dd} de {calendario[mm]} de {aaaa}.")

#Ejercicio Nro5 - Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total = 0
for asignatura, creditos in asignaturas.items():
    print(f"{asignatura} tiene {creditos} créditos.")
    total += creditos

print(f'El número total de créditos del curso es de: {total}')

'''
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un 
diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del 
cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un 
cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú:

(1) Añadir cliente: Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
(2) Eliminar cliente: Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
(3) Mostrar cliente: Preguntar por el NIF del cliente y mostrar sus datos.
(4) Listar todos los clientes: Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
(5) Listar clientes preferentes: Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
(6) Terminar: Salir del Programa.
'''
clientes = {}

def agregar_cliente(nif,nombre, direc, tlf, mail, pref):
    datos_cliente = {"Nombre": nombre, "Dirección":direc, "Teléfono":tlf, "Correo Electrónico":mail, 'Cl. Preferente':pref}
    clientes[nif] = datos_cliente

    return f"Se ha agregado el cliente correctamente {nombre} a la BBDD. "

def eliminar_cliente(nif, nombre):
    if nif in clientes.keys():
        del clientes[nif]
        
        return f'Se ha borrado {nombre} de la BBDD.'

    else:
        print("Cliente Inexistente...")

def mostrar_cliente(nif):
    print(f"NIF: {nif}")
    if nif in clientes:
        for i, j in clientes[nif].items():
            print(i + " : " + j)  
    else:
        print("Cliente Inexistente...")

def listar_clientes():    
    try:
        if nif in clientes:        
            for i, j in clientes.items():
                print(i, j["Nombre"])  
    
    except NameError:
        print("No hay datos registrados en la BBDD")

def clientes_preferentes():
    try:
        for i , j in clientes.items():
            if i['Preferente']:
                print(i, j["Nombre"])  
    
    except:
        print("No hay Clientes Preferentes en la BBDD")


print("""
Menú:
-(Usar 1) Para Agregar un cliente a la BBDD.
-(Usar 2) Para Eliminar un cliente de la BBDD.
-(Usar 3) Para Mostrar un cliente en específico.
-(Usar 4) Para Listar Todos los clientes de la BBDD.
-(Usar 5) Para Listar Solamente los Clientes Preferentes.
-(Usar 6) Para Salir del programa.
""")

while True:
    try:
        opcion = int(input("\nEsperando una respuesta: "))
    
    except ValueError:
        print("ERROR! Debe ingresar la opción como lo indica el menú...")
    else:
        if opcion == 1:
            nif = input("Introduce el NIF del cliente: ")
            nomb = input("\nIngrese el Nombre del cliente: ")
            direc = input("Ingrese la Dirección: ")
            tlf = input("Ingrese el Número de Teléfono del cliente: ")
            correo = input("Ingrese el Correo Electrónico del cliente: ")
            pref = input("Ingrese usando 'True'(Si/Verdadero) o 'False'(No/Falso) si la persona es un Cliente Preferente: ")
            print(agregar_cliente(nif, nomb,direc,tlf,correo,pref))
        
        elif opcion == 2:
            nif = input("Ingrese el NIF del cliente que desea Eliminar: ")
            nombre = input("Ingrese su nombre: ")
            print(eliminar_cliente(nif, nombre))

        elif opcion == 3:
            nif = input("Ingrese el NIF del Cliente que desea Mostrar sus Datos: ")            
            print(mostrar_cliente(nif))
        
        elif opcion == 4:
            print("Todos los Clientes:\n")
            print(listar_clientes())

        elif opcion == 5:
            print("Todos los Clientes Preferentes:\n")
            print(clientes_preferentes())
        
        elif opcion == 6:
            print("Programa Cerrado.")
            break

        else: 
            print("ERROR!")