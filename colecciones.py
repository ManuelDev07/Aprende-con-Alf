import random

#Ejercicio Nro1 - Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
materias = []
while True:
    opcion = input("¿Desea Registrar Materias? S/N: ").lower()

    if opcion == 's':
        registro = input("\nRegistra las asignaturas de tu curso: ")
        materias.append(registro)
    elif opcion == 'n':
        print("\nLas Materias registradas son: ")
        print(materias)
        break
    else: 
        print("\nERROR! Debe seleccionar S o N.")

#Ejercicio Nro2 - Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
while True:
    opcion = input("¿Desea Registrar Materias? S/N: ").lower()

    if opcion == 's':
        registro = input("\nRegistra TODAS las asignaturas de tu curso usando una ',': ").replace(","," ").split()
    elif opcion == 'n':
        for materia in registro:
            print(f"Yo estudio {materia} ")
        break
    else: 
        print("\nERROR! Debe seleccionar S o N.")

#Ejercicio Nro3 - Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
while True:
    opcion = input("""
Menú:
-(Usar R) para Registrar las asignaturas.
-(Usar N) para mostrar TODAS tus notas.
-(Usar S) para salir del programa.
""")

    if opcion.upper() == 'R':
        asignatura = input("\nRegistra TODAS las asignaturas de tu curso usando una ',': ").replace(","," ").split()
    
    elif opcion.upper() == 'N':
        for materia in asignatura:
            x = random.randint(0, 10)
            print(f"En {materia} has sacado {x} ")
                
    elif opcion.upper() == 'S':
        print("Hasta Pronto.")
        break
    
    else: 
        print("\nERROR! Debe seleccionar S o N.")

#Ejercicio Nro4 - Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
lista = []

while True:
    numeros = int(input("Ingrese los números ganadores de la loteria: "))
    lista.append(numeros)

    salir = input('\nSi quiere salir del programa, ingrese solamente "Q"')
    if salir.upper() == 'Q':
        break

print(f"Los numeros ganadores son: {lista.sort()} ")

#Ejercicio Nro5 - Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
gg = []
for i in range(0,10):
    gg.append(i + 1)

gg.reverse()
print(gg)
'''
#Ejercicio Nro6 - Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
while True:
    opcion = input('''