'''
Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
divisibles por 5, y la suma de los enteros generados que sean impares.
'''
n = 2
max = 30

while n < max:
    n % 3
    if n == max:
        break
    print(n)
