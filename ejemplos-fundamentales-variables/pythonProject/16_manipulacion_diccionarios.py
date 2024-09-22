# Manipulación de diccionarios
person = {
    'name': 'Daniel',
    'last_name': 'Condía Figueredo',
    'langs': ['Python', 'PHP', 'Java'],
    'age': 19
}

print(person)

# Para editar un valor
person['name'] = 'Otro nombre'
person['age'] -= 10
person['langs'].append('JavaScript')
print(person)

# Para eliminar un valor en un diccionario
del person['last_name']

# También se puede con el método pop, pero pop recibe obligatoriamente un dato
person.pop('age')

print(person)

"""
items, keys y values en diccionarios.
items en los diccionarios nos devuelve pares de tuplas, por ejemplo
(clave: valor) (clave: valor) nos devuelve en tuplas las claves y los valores del
diccionario.
Las keys solo nos devuelve las llaves del diccionario
y vales nos devuelve los valores que tiene el diccionario
"""

print('Items:')
print(person.items())

print('Keys:')
print(person.keys())

print('Values:')
print(person.values())
