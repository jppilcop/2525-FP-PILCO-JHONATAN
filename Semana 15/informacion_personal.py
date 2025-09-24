# 1. Creacion de un diccionario
informacion_personal = {
    "Nombre": "Paúl Pilco",
    "Edad": 30,
    "Ciudad": "Quito",
    "Profesion": "Licenciado en Matemática y Física"
}

# 2. Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] = "Quito"

# 3. Agregar una nueva clave-valor para la profesion (actualizar profesión)
informacion_personal["Profesión"] = "Estudiante TIC"

# 4. Verificar si la clave "telefono" existe, si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0983863031"

# 5. Eliminar la clave "edad"
informacion_personal.pop("edad", None)  # el None evita error si no existe

# 6. Imprimir el diccionario final
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")