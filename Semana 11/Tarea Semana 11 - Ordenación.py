# Ordenación de Arreglo Multidimensional

# Definimos una matriz 3x3
matriz = [
    [9, 4, 7],
    [2, 8, 6],
    [5, 1, 3]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Elegir qué fila ordenar (ejemplo: fila 1 → índice 0)
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz después de ordenar la fila", fila_a_ordenar, ":")
for fila in matriz:
    print(fila)