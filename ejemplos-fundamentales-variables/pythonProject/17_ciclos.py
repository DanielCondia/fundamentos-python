# Ciclos ejemplo de while
"""
contador = 0
while contador < 20:
    contador += 1
    print(contador)
"""
# Ejemplo de ciclos for
# range da un rango de números que es la cantidad de veces que queremos iterar
"""
for element in range(20):
    print(element)
"""    
# Con range también podemos darle un inicio y un fin
"""
for element in range(2, 21):
    print(element)
"""    
# Recorriendo listas
my_list = [23, 45, 46, 78, 50]
for i in my_list:
    print(i)
    
print("*"*20)

# Recorriendo tuplas
my_tuple = ("Es", "una", "tupla")
for i in my_tuple:
    print(i)
print("*"*20)

# Recorriendo un diccionario
product = {
    'name': 'Camiseta',
    'price': 2000,
    'stock': 90
}
print("*"*20)

for key in product:
    print(key)
    print(key, '=>', product[key])
print("*"*20)

# Manera corta
for key, value in product.items():
    print(key, '=>', value)

