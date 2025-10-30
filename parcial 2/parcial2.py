def invertir_array(array):
    return array[::-1]

# Solicitar la cantidad de elementos
n = int(input("¿Cuántos elementos tendrá el arreglo?: "))

# Solicitar los elementos del array
array = []
for i in range(n):
    elemento = input(f"Ingresa el elemento {i+1}: ")
    array.append(elemento)

array_invertido = invertir_array(array)

print("Array original:", array)
print("Array invertido:", array_invertido)