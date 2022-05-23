import math
import statistics

#Ejercicio Nro1 - Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
def hola():
    print("Hola Amiga!")

hola()

#Ejercicio Nro2 - Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.


def saludo(nombre):
    print(f"Hola {nombre}")

nomb = input("Ingrese su nombre: ") 
saludo(nomb)

#Ejercicio Nro3 - Escribir una función que reciba un número entero positivo y devuelva su factorial.
def fact(numero):
    resultado = 1
    for i in range(numero):
        resultado *= i + 1
    
    print(resultado)

fact(7)

#Ejercicio Nro4 - Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
def factura(precio, iva=0.21):
    '''Función para aplicar el total del IVA a un producto
    Parámetros:
    precio : el costo del producto
    iva: el porcentaje del IVA
    Se devolverá el total de la factura luego de aplicarse el IVA
    '''
    
    print(f"El total a pagar es de:{precio * iva}$") 

precio = float(input("Ingrese el precio del producto: "))
factura(precio,0.19)

#Ejercicio Nro5 - Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def area_circulo(radio):
    pi = math.pi
    return pi * radio**2

def volumen_cilindro(radio, altura):
    print(f"El volumen del cilindro es de: {area_circulo(radio)*altura:.3f} ")

print("Volumen del Cilindro:")
r = float(input("Ingrese el radio del cilindro: "))
h = float(input("Ingrese la altura del cilindro: "))
volumen_cilindro(r,h)


#Ejercicio Nro6 - Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(lista):
    resultado =  sum(lista) / len(lista)
    return resultado

print(media([1,2,3,4,5,6,56,132,1,6,9,11,150]))

#Ejercicio Nro7 - Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrados(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero**2)

    return nueva_lista

print(cuadrados([1,2,3,4,5,6,7,8,9,10]))
