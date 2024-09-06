"""
En python podemos usar indexing,
que es tratar el texto directamente como si fuera un arreglo.
"""
text = "El sabe Pyton"
print(text[0])

# Para ingresar al último caracter del texto
print(text[len(text) - 1])

"""
Otra alternativa es escribir directamente la posición negativa. Python comienza desde la última palabra hacia atrás
"""
print(text[- 1])

# slicing, obtiene un trozo del texto con las longitudes que nosotros especifiquemos
print(text[2:5])
print(text[:10]) # por defecto viene en 0 si no se específica
print(text[5:]) # por defecto va hasta el final del texto si no se específica
print(text[:]) # Teniendo en cuenta lo anterior, podemos usar esta sintaxis


