#Ejercicio Nro1 - Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
palabra = input("Ingrese una palabra: ")

for i in range(10):
    print(palabra)

#Ejercicio Nro2 - Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
edad = int(input("Ingrese su edad: "))

for edades in range(1, edad + 1):
    print(f"{edades} año(s).")

#Ejercicio Nro3 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
numero = int(input("Ingrese un número entero positivo: "))

for i in range(1, numero + 1, 2):
    if i == numero:
        print(i, end='.')
    else: 
        print(i, end=', ')

#Ejercicio Nro4 - Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
negativo = int(input("Ingrese un número entero positivo: "))

for i in range(negativo, -1, -1):
    if i == 0:
        print(i, end='.')
    else: 
        print(i, end=', ')

#Ejercicio Nro6 - Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
filas = int(input("Ingrese un número entero positivo el cuál será la altura del triángulo: "))

for i in range(filas):
    for j in range(i + 1):
        print('🟩', end='')
    print(" ")

#Ejercicio Nro7 - Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
print("Tablas de Multiplicar del 1 al 10:")

for i in range(1, 10):
    print(f"Tabla del {i}:")    
    for j in range(0, 11):
            print(f"{i} x {j} = {i * j}")
    
    print('')

#Ejercicio Nro9 - Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
while True:
    password1 = "contraseña"
    password2 = input("Ingrese la Contraseña: ").lower()

    if password2 == password1:
        print("Acceso Concedido! :D")
        break
    else:
        print("Acceso Denegado :(")


#Ejercicio Nro10 - Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
try:
    x = 2
    number = int(input("Ingrese un número entero positivo para verificar si es primo o no: "))
    while (number % x) != 0: 
        x += 1
    
    if x == number:
        print(f"El Número {number} SI es considerado un Número Primo.")
    else:
        print(f"El Número {number} NO es considerado un Número Primo.")        

except ValueError:
    print("ERROR! Debe ingresar el dato que se le pide... -_-")

#Ejercicio Nro 11 - Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input("Ingrese una palabra: ")

for letra in palabra[::-1]:
    print(letra)

#Ejercicio Nro 12 - Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase a evaluar: ").lower()
letra = input("ingrese una letra de la frase que quiere contar: ").lower()

for i in frase:
    cont = frase.count(letra)

print(f"El total de letras que aparecen repetidas en la frase {frase} ha sido de: {cont}")

#Ejercicio Nro 13 - Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
while True:
    eco = input("Ingrese un texto: ")

    if eco.lower() == 'salir':
        break
    else:
        print(eco)