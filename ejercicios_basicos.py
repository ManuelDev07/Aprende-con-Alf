import math

#Ejercicio Nro1 - Imprimir un "Hola Mundo"
print("Hola Mundo")
print("-" * 50)

#Ejercicio Nro2 - Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
saludo = "Hola Mundo desde una Variable"
print(saludo)
print("-" * 50)

#Ejercicio Nro3 - Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido
saludo1 = input("Ingrese su nombre: ")
print(f"Hola {saludo1}")
print("-" * 50)

#Ejercicio Nro4 - Operación Matemática.
p1 = (3+2)/(2*5)
p2 = p1 ** 2
p3 = (((3+2)/(2*5)) ** 2)
print(p3)
print("-" * 50)

#Ejercicio Nro5 - Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
while True:
    try:
        horas = int(input("Ingrese el numero de horas trabajadas: "))
        sueldo = float(input("Ingrese el coste en $ por hora: "))
        print(f"La paga que recibirá será de: {horas*sueldo}$")
        print("-" * 50)
        break

    except ValueError:
        print("ERROR! Solo debe ingresar números :(")

#Ejercicio Nro6 -Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
try:
    num = int(input("Ingrese un numero para sumar: "))
    suma = ((num * (num + 1)) / 2)
    print(suma)
    print("-" * 50)
except:
    print("ERROR! Deben ser solo números enteros")
    print("-" * 50)


#Ejercicio Nro7 - Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
peso = float(input("Ingrese su peso en kilogramos (kg): "))
estatura = float(input("Ingrese su estatura en metros (m): "))
imc = (peso *(estatura ** 2))
print(f"Tu índice de masa corporal es de {imc:.2f} ")

print("-" * 50)

#Ejercicio Nro8 - Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
n = int(input("Ingrese el Primer Número a Dividir: "))
m = int(input("Ingrese el Segundo Número a Dividir: "))
c = n / m
r = n % m

print(f"El resultado de la división es: {c}(Cociente) y se resto es: {r}")

'''Ejercicio Nro9 - Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística 
les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g 
y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que 
será enviado.
'''

def jugueteria(num_payasos, num_munecas):
    peso_total_payasos = num_payasos * 112
    peso_total_munecas = num_munecas * 75
    peso_total_envio = peso_total_munecas + peso_total_payasos

    return print(f"El Peso Total del Paquete es de: {peso_total_envio}gr. Con {num_payasos} Payasos y {num_munecas} Muñecas")



while True:
    opcion = input('''
MENÚ:
-(Ingresar P) Para Registrar las ventas de un Producto.     
-(Ingresar Q) Para Salir del programa.
''').upper()
    
    if opcion == "P":
        num_munecas = int(input("¿Cuantas Muñecas serán despachadas?: "))
        num_payasos = int(input("¿Cuantos Payasos serán despachados?: "))
        llamar = jugueteria(num_payasos, num_munecas)
        break
    else:
        print("Hasta Pronto :(")
        break