def imprimir_lista(mensaje, lista):
    print(mensaje, lista)
    
# CRUD

numbers = [1,2,3,4,5]
imprimir_lista("Lista de números => ", numbers)

numbers[-1] = 10
imprimir_lista("Modifica posición específica => ",numbers)

# Para agregar un nuevo valor al final de la lista
numbers.append(700)
imprimir_lista("Se agrega un nuevo valor en lo último de la lista => ",numbers)

# Para insertar un nuevo dato en la lista. No se eliminá el anterior dato
numbers.insert(0, 'Hola')
imprimir_lista("Agregar nuevo dato con insert => ", numbers)

numbers.insert(3, 'Changes')
imprimir_lista("Agregar nuevo dato con insert => ", numbers)

# Para fusionar listas 
tareas = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4"]
nueva_lista = tareas + numbers
imprimir_lista("Fusionar listas => ", nueva_lista)

# Para obtener el index dentro de una lista según el valor
index = nueva_lista.index("Tarea 4")
imprimir_lista("Buscando index a través de valor => ", index)

# Para remover datos de la lista
nueva_lista.remove("Tarea 1")
imprimir_lista("Removiendo elementos => ", nueva_lista)

# Remueve el último valor de la lista
nueva_lista.pop()
imprimir_lista("Removiendo el último elemento de la lista => ", nueva_lista)

nueva_lista.pop(0) # pop también recibe un index para eliminar el elemento

# Voltear un arreglo
nueva_lista.reverse()
imprimir_lista("Volteando lista => ", nueva_lista)

# Ordenando números con sort
numbers_b = [5,4,3,2,1]
numbers_b.sort()
imprimir_lista("Ordenando con sort => ", numbers_b)

# Ordenando lista de string en orden alfabético
strings_abc = ["re", "ab", "ed"]
strings_abc.sort()
imprimir_lista("Ordenando alfabeto => ", strings_abc)

