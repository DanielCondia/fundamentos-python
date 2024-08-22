"""
 Algo importante de tener en cuanta a la hora de escribir strings, es cuando tenemos unas comillas simples
 entre el string, y el string lo escribimos justo con las comillas simples, o viceversa.
"""

string_simple = "I'm Daniel"  # Tener en cuenta la comilla simple del I'm... Si escribiéramos ese string con '',
# estaría mal

string_complex = 'She said: "Hellooo"'  # Ahora tengamos en cuenta que aquí es todo lo contrario.

print(string_simple)
print(string_complex)

# Ahora la parte del formato para imprimir strings

my_name = "Daniel"
my_last_name = "Condía Figueredo"
my_age = 18

# Varias formas de dar formato, de la más complicada y menos sofisticada a la más sencilla que es la última y más
# sofisticada

# Con la función str pasamos tipo numérico a string
rta1 = "Mi nombre es " + my_name + " " + my_last_name + " y tengo " + str(my_age)
print(rta1)

# Segundo método
rta2 = "Mi nombre es {} {} y tengo {}".format(my_name, my_last_name, my_age)
print(rta2)

# Tercer método y más efectivo
rta3 = f"Mi nombre es {my_name}{my_last_name} y tengo {str(my_age)}"
print(rta3)
