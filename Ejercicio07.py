#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delantera de la arroba @) pero con dominio ceu.es.
correo = input('¿Cual es tu correo electronico?')
correo2 = correo.split('@')[0]
correo3 = (correo2 + '@ceu.es')
print('Tu nuevo correo electronico es: ', correo3)