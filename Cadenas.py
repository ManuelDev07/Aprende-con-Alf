#Ejercicio Nro1 - Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''
try:
    nombre = input("Ingrese su nombre: ")
    num = int(input("Ingrese un numero: "))
    
    for i in range(0, num):
        print(nombre)

except ValueError:
    print("ERROR! Debe ingresar los datos como se le indica... Intente de nuevo. :(")

#Ejercicio Nro2 - Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
 
nomb = input("Registre su nombre COMPLETO (Nombres y Apellidos): ")
print(nomb.upper())
print(nomb.lower())
print(nomb.title())

#Ejercicio Nro3 - Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
NOMBRE = input("Ingrese su nombre: ")
cont = 0

for i in NOMBRE.replace(" ", ""):
    cont += 1

print(f"Tu nombre: {NOMBRE.upper()} tiene {cont} letras.")

#Ejercicio Nro4 - Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
print("Formato: +prefijo-número-extension | +xx-xxxxxxx-xx")
numero = input("Ingresa tu número telefónico como se muestra su formato: ")
print(numero[4:-3])

#Ejercicio Nro5 - Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
frase = input("Ingrese una frase o palabra: ")
frase = frase.replace(" ","")
frase_invertida = frase[::-1]
print(frase_invertida)

#Ejercicio Nro6 - Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = input("Ingrese una frase o palabra: ")
vocal = input("Ingrese la vocal que quiere ver en Mayúscula dentro del texto ingresado anteriormente: ")
vocal_nueva = vocal.upper()

frase_nueva = frase.replace(vocal, vocal_nueva)
print(frase_nueva)

#Ejercicio Nro7 - Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio unet.edu.ve.
mail = input("Ingrese su correo electrónico: ")
verificarGmail = mail[-9:]
verificarOtro = mail[-11:]

if verificarGmail == "gmail.com":
    mail_nuevo = mail.replace(verificarGmail, "unet.edu.ve")
    print(mail_nuevo)

elif verificarOtro == "outlook.com" or "hotmail.com":
    mail_nuevo = mail.replace(verificarOtro, "unet.edu.ve")
    print(mail_nuevo)

#Ejercicio Nro8 - Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Ingrese el precio del producto con sus dos decimales: ")
enteros = precio[:-3]
decimales = precio[-2:]

print(f"Los números enteros del precio son: {enteros}€ con: {decimales} céntimos")

#Ejercicio Nro9 - Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
print("El formato es: dd/mm/aaaa")
nacimiento = input("Ingrese la fecha de su nacimiento: ")

if len(nacimiento) == 10:
    dd = nacimiento[:2]
    mm = nacimiento[3:5]
    aaaa = nacimiento[-4:]
    print(f"Naciste el DÍA {dd} del MES {mm} del AÑO {aaaa}")

else:     
    dd = nacimiento[:1]
    mm = nacimiento[2:3]
    aaaa = nacimiento[-4:]
    print(f"Naciste el DÍA {dd} del MES {mm} del AÑO {aaaa}")
'''
#Ejercicio Nro 10 - Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
productos = input("Ingrese los productos que ha comprado separados por comas: ")
for producto in productos.split(","):
    print(producto)
    
