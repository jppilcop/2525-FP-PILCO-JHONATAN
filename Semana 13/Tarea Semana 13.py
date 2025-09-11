def calcular_promedio_temperaturas(datos_ciudades):
    """
    Calcula el promedio de temperatura de cada ciudad a partir de sus registros semanales.

    Parámetros:
        datos_ciudades (dict): Diccionario con las ciudades como claves
                               y listas de temperaturas (semanales) como valores.

    Retorna:
        dict: Diccionario con el promedio de temperatura de cada ciudad.
    """
    promedios = {}
    for ciudad, temperaturas in datos_ciudades.items():
        if len(temperaturas) > 0:
            promedio = sum(temperaturas) / len(temperaturas)
        else:
            promedio = None  # En caso de que no haya datos
        promedios[ciudad] = promedio
    return promedios


# Ejemplo de uso con 3 ciudades y 4 semanas
datos = {
    "Quito": [18, 20, 19, 21],  # Semana 1 a 4
    "Ibarra": [17, 18, 16, 19],
    "Riobamba": [15, 14, 16, 15]
}

resultado = calcular_promedio_temperaturas(datos)

print("Promedio de temperaturas por ciudad:")
for ciudad, promedio in resultado.items():
    print(f"{ciudad}: {promedio:.2f} °C")
