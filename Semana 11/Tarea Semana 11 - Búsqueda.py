# Búsqueda en Arreglo Multidimensional

# Definimos una matriz 3x3
matriz = [
    [5, 8, 12],
    [7, 3, 9],
    [6, 4, 10]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (fila, columna)
    return None

# Valor a buscar
valor_buscado = 9

resultado = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"BIEN El valor {valor_buscado} se encontró en la posición (fila={resultado[0]}, columna={resultado[1]}).")
else:
    print(f"MAL El valor {valor_buscado} no se encontró en la matriz.")