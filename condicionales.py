#Ejercicio Nro1- Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        
        if edad >= 18:
            print("Mayor de edad.")
            break
        
        else:
            print("Menor de edad.")
            break
    
    except ValueError:
        print("ERROR! Debe ingresar un NÚMERO.")

#Ejercicio Nro2 - Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
x = "contraseña"
y = input('Ingrese la palabra "contraseña": ').lower()

if x == y:
    print("CORRECTO!")

else:
    print('ERROR!')

#Ejercicio Nro - Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
divid = int(input("Ingrese el Dividendo: "))
divis = int(input("Ingrese el Divisor: "))

if divis == 0:
    print("ERROR! No puede dividirse entre 0")

else:
    resultado = divid / divis
    print(f"El resultado es: {resultado}")

#Ejercicio Nro4 - Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
try: 
    num = int(input("Ingrese un número entero: "))
    
    if num % 2 == 0:
        print(f"El número {num} es PAR.")

    else:
        print(f"El número {num} es IMPAR.")

except:
    print("ERROR! Debe ingresar un número ENTERO.")

#Ejercicio Nro5 - Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
age = int(input("Ingrese su edad: "))
ing_mensual = float(input("Ingrese sus ingresos mensuales: "))

if age > 16 and ing_mensual >= 1000:
    print("Tiene que tributar.")

else:
    print("No tiene que tributar. :D")

#Ejercicio Nro6 - Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
grupoA = []
grupoB = []

while True:
    opcion = input("¿Desea registrar o salir? R/S: ").upper()
    
    if opcion == 'R':
        nombre = input("Registre su nombre: ").upper()
        sexo = input("¿Que género es? F/M: ").upper()

        if nombre < 'M' and sexo == 'F':
            print(f'{nombre.title()} irá al grupo "A" ')
            grupoA.append(nombre)

        elif nombre > 'N' and sexo == 'M':
            print(f'{nombre.title()} irá al grupo "A" ')
            grupoA.append(nombre)

        else:
            print(f'{nombre.title()} irá al grupo "B" ')
            grupoB.append(nombre)
    
    elif opcion == 'S':
        break

print(f"Grupo A: {grupoA}")
print(f"Grupo B: {grupoB}")


'''
Ejercicio Nro7:
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
    Renta:              |   Tipo impositivo
-Menos de 10000€        | -5%
-Entre 10000€ y 20000€  | -15%
-Entre 20000€ y 35000€  | -20%
-Entre 35000€ y 60000€	| -30%
-Más de 60000€          | -45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
'''
try:
    renta = float(input("Para la declaración Tipo Impositivo por favor ingrese su Renta Anual: "))

    if renta < 10000:
        print(f"Deberá pagar: {renta * 0.5}€") 

    elif  10000 < renta <= 20000: 
        print(f"Deberá pagar: {renta * 0.15}€") 

    elif  20000 < renta <= 35000: 
        print(f"Deberá pagar: {renta * 0.20}€")

    elif  35000 < renta <= 60000: 
        print(f"Deberá pagar: {renta * 0.30}€")
    
    else:
        print(f"Deberá pagar: {renta * 0.45}€")        

except:
    print("ERROR! Por favor ingrese el dato como se le indica.")


#Ejercicio Nro9 - Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
cliente = int(input('''
Bienvenid@ a la sala de juegos!

Ingrese su edad: '''))

if cliente < 4:
    print("Entrada Gratuita.")
elif 4 <= cliente <= 18:
    print("Precio de la Entrada: 5€") 
else:
    print("Precio de la Entrada: 10€")