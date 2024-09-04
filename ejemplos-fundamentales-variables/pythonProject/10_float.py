"""
En Python se debe tener cuidado a la hora de hacer algunas operaciones con float, ya que python suele tener
más décimales de los que pensamos normalmente
"""

x = 3.3
print(x)

y = 1.1 + 2.2
print(y)
print(x == y)

"""
Una de las maneras de soluciones esto, es pasar el valor que queremos comparar a string
En este caso se usa la función format, su segundo parametro significa el número de dígitos que se quiere dejar
"""
y_str = format(y, ".2g")
print("str => ", y_str)
print(y_str == str(x))

print('*' * 20)

# Hacemos la comparación ahora de manera más matemática
tolerance = 0.00001
print(abs(x - y) < tolerance)