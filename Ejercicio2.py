'''
Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
mayores a 7.0.
'''
print("Ingrese las notas de la asignatura de programación(maximo 10)") 

n1 = float(input("Ingrese la nota: "))
if n1 < 1 :
    print("Nota inferior a 1.0")
elif n1 > 7 :
    print("Nota inferior a 7.0")

n2 = float(input("Ingrese la nota: "))
if n2 < 1 :
    print("Nota inferior a 1.0")
elif n2 > 7 :
    print("Nota inferior a 7.0")

n3 = float(input("Ingrese la nota: "))
if n3 < 1 :
    print("Nota inferior a 1.0")
elif n3 > 7 :
    print("Nota inferior a 7.0")

n4 = float(input("Ingrese la nota: "))
if n4 < 1 :
    print("Nota inferior a 1.0")
elif n4 > 7 :
    print("Nota inferior a 7.0")

n5 = float(input("Ingrese la nota: "))
if n5 < 1 :
    print("Nota inferior a 1.0")
elif n5 > 7 :
    print("Nota inferior a 7.0")

n6 = float(input("Ingrese la nota: "))
if n6 < 1 :
    print("Nota inferior a 1.0")
elif n6 > 7 :
    print("Nota inferior a 7.0")

n7 = float(input("Ingrese la nota: "))
if n7 < 1 :
    print("Nota inferior a 1.0")
elif n7 > 7 :
    print("Nota inferior a 7.0")

n8 = float(input("Ingrese la nota: "))
if n8 < 1 :
    print("Nota inferior a 1.0")
elif n8 > 7 :
    print("Nota inferior a 7.0")

n9 = float(input("Ingrese la nota: "))
if n9 < 1 :
    print("Nota inferior a 1.0")
elif n9 > 7 :
    print("Nota inferior a 7.0")

n10 = float(input("Ingrese la nota: "))
if n10 < 1 :
    print("Nota inferior a 1.0")
elif n10 > 7 :
    print("Nota inferior a 7.0")



lista = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
listadef = lista.append
print(listadef)

suma = sum(lista)

media = suma/10
print(media)