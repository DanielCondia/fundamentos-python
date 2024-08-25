"""
En python la transformación de los datos se puede hacer de manera dinámica directamente sin necesidad
de un método o función intermedio.

Por ejemplo en este caso se establece una variable name de tipo string, y en seguida se cambia
el valor de esta variable a tipo int sin necesidad de hacer un cast o conversión con una función.
Así se puede hacer con cualquier tipo de dato, también a boolean
"""

name = "Daniel"
print(type(name))
name = 18
print(type(name))
name = True
print(type(name))

"""
En Python a la hora de concatenar o sumar los datos, hay que tener cuidado con el tipo de dato.
Por ejemplo, no se puede concatenar un número con un string. Para poder hacer ello, se debe pasar al mismo
tipo de dato. Se va a sumar o concatenar correctamente siempre y cuando sea del mismo tipo de dato
"""

print("Hola " + "Daniel")
print(10 + 20)
# print("Edad " + 20) éste print va a dar error

"""
Para poder pasar un númer a string y poder concatenar el valor numérico a un string, se puede usar la función
str(int). Con esto podemos pasar un valor numérico y la funión devuelve un string para poder concatenarlo.

Otras de las maneras de poder usar un valor numérico concatenado, es usar el format string con la
f antes del string y concatenando los valores con {}
"""

age = 19
print("Mi edad es: " + str(age))
print(f"Mi edad es: {age}")

"""
Ahora el caso contrario, si queremos pasar un string a tipo numérico y lo queremos imprimir
"""

edad = input("Ingresa tu edad => ")
edad = int(edad)
print(f"Tu edad en 10 años será => {edad + 10}")
