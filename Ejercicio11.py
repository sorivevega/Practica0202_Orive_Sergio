#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input('¿Que has comprado? ')
precio = float(input('¿Cuanto cuesta? '))
x = round(precio, 2)
unidades = int(input('¿Cuantos has comprado? '))
total = float(x * unidades)
print('El producto {} vale {:9.2} y quiero {:3d} unidades. El total es {:11}'.format(producto, x, unidades, round(total, 2)))