#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
frase = input('Introduzca una frase: ')
letra = input('Escriba una vocal que perteneca a su frase: ')
frase2 = frase.replace(letra, letra.upper())
print(frase2)