#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fecha = input('Introduce tu fecha de cumpleaños')
dia = (fecha[0:2])
mes = (fecha[3:5])
año = (fecha[6:10])
n = fecha.split('/')
d = n[0] 
m = n[1]
a = n[2]
print('Tu cumpleaños es el dia {d} , del mes {m} , del año {a}'.format(dia, mes, año))