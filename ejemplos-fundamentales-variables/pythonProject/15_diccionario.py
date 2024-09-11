"""
En Python existe el concepto de diccionario.
Prácticamente, es como un objeto que tiene llave valor, en el que se define como un objeto json.
La ventaja es que se pueden usar funciones comunes para la fácil manipulación de los datos
"""

my_dictionary = {
    'Clave': 'Valor',
    'age': 18
}

print(my_dictionary)
# Podemos acceder a un valor como si fuera un arreglo a través de la llave. No es recomendable acceder así
print(my_dictionary['age'])

"""
Es recomendable que si queremos acceder a un valor a través de la llave, usemos la función .get().
Esto es porque dado el caso de que la llave no exista, el .get no nos arroja un error, si no que nos da un valor
none, no existe la clave. De lo contrario si lo hacemos con [], nos arroja una excepción y se estalla todo el código
"""
print(my_dictionary.get('fdsgdf')) # simula un valor que no existe

# También se puede verificar con in
print('avion' in my_dictionary)
print('age' in my_dictionary)

print(my_dictionary['ffasdf']) # simula un valor que no existe
