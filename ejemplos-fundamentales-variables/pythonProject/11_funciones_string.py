text = 'Ella sabe programar en Python'
# Busca si una palabra o cadena de caracteres se encuentra dentro de otro texto
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print("Si tiene Python")
else:
    print("No tiene Python")
    
# Cuenta la longitud de la cadena
size = len(text)
print(f"Tamaño => {size}")

# Upper y Lower
print(text.upper())
print(text.lower())

# Cuenta cuantas veces se repite una palabra dentro de un string
print(text.count('a'))

# Invierte mayusculas y minusculas
print(text.swapcase())

# Verificamos si un string inicia o termina con una palabra en especifico
print(text.startswith('Ella'))
print(text.endswith('Rust'))

# Reemplaza una palabra con otra
print(text.replace('Python', 'Go'))

# Coloca el primer caracter de un string en mayuscula
text_2 = "este es un titulo"
print(text_2.capitalize())

# Coloca el primer caracter de cada palabra dentro de un string en mayuscula
print(text_2.title())

# Verifica si un string es un posible digito
print(text_2.isdigit())
print("4234".isdigit())