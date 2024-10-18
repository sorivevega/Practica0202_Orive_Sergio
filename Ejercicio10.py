#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
lista = input('¿Que has comprado hoy?: ')
n = lista.split(',')
x = len(n)
y = 0
while x > 0:
    print(n[y])
    y = y + 1
    x = x - 1