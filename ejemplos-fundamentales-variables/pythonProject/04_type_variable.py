# La función type nos permite ver el valor de una variable

my_name = "Daniel"
print("El nombre: ", my_name, " es de tipo => ", type(my_name))  # El valor de my name

my_age = 18
print("La edad: ", my_age, " es de tipo => ", type(my_age))  # El valor de my age

# Cuando recibimos un valor con la función input, siempre vamos a recibir un str = string
my_input = input("Introduce your value ")
print("The value of input is: ", my_input, type(my_input))

# Para variables de tipo boolean, siempre el valor comienza en mayúscula

my_boolean = True
my_two_boolean = False

print(type(my_boolean), type(my_two_boolean))
