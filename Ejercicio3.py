'''
Se cuenta con dos sets, los cuales contienen precios de productos: (40 Puntos)
Set 1 = {100, 250, 300, 1000}
Set 2 = {150, 250, 500, 1000}
A) Verificar si el valor 100 está en ambos sets
B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
C) Elevar a 3 todos los valores dentro de los sets
D) Unir ambos sets en uno solo
'''

Set1 = {100, 250, 300, 1000}
Set2 = {150, 250, 500, 1000}

#A)
print("Set 1")

for a in Set1:
    print(a)

if 100 in Set1:
    print("Se encuentra el número 100")
else:
    print("No se encuentra el número 100")

print("Set 2")

for b in Set2:
    print(b)

if 100 in Set2:
    print("Se encuentra el número 100")
else:
    print("No se encuentra el número 100")

#B)

if 500 in Set1:
    print("En el set Número 1 si se encuentra el número 500")
else:
    print("En el set Número 1 no se encuentra el número 500")

if 700 in Set1:
    print("En el set Número 1 si se encuentra el número 700")
else:
    print("En el set Número 1 no se encuentra el número 700")

if 500 in Set2:
    print("En el set Número 2 si se encuentra el número 500")
else:
    print("En el set Número 2 no se encuentra el número 500")

if 700 in Set2:
    print("En el set Número 2 si se encuentra el número 700")
else:
    print("En el set Número 2 no se encuentra el número 700")

#C)



#D)


