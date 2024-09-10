# Las tuplas son datos inmutables. Se inicializan con parentesis
numbers = (1,2,3,4,4)
strings = ('D', 'a', 'n', 'i', 'e', 'l', 'D')
print(strings)
print(type(numbers))

"""
Las tuplas naturalmente son inmutables por ende no podemos manipularlas igual que un
arreglo. No podemos insertar y actualizar datos que ya estan dentro de la tupla, pero
si podemos ejecutar más métodos para obtener indices o estadisticas de datos
"""
print(strings.count("D")) # Verifica cuantas veces se repite
print(numbers.count(4)) # Verifica cuantas veces se repite
print(strings.index("D")) # Obtiene el indice

"""
Dado el caso que necesitemos editar algún dato de una tupla, podemos hacer un cast
o convertir la tupla a una lista para poder modificar los datos
"""

my_list = list(strings) # Convertimos la tupla en lista
print(my_list)
print(type(my_list))

# Para convertir de lista a tupla

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))