#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
dinero = input('¿Cuanto vale lo que acabas de comprar?')
euros, centimos = dinero.split('.')
print('El producto que acabas de comprar vale', euros, '€', 'y', centimos, 'centimos')