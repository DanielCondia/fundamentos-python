print("Hello World")
# Esto es un comentario

'''
Esto es un comentario de
varias lineas.
Podemos usar cuantas lineas queramos
'''

deuda = 1000000
interes = 0.028
cuotas = 12
valor_mensual = deuda*(interes*(1+interes)**cuotas) / ((1+interes)**cuotas-1)
print(valor_mensual)