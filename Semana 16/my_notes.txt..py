# Tarea: Trabajo con Archivos de Texto en Python

# 1. Escritura de Archivo de Texto

archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales usando el método write()
archivo.write("Nota 1: Levantarme de lunes a viernes a las 06:00.\n")
archivo.write("Nota 2: Llegar al trabajo a las 06:45.\n")
archivo.write("Nota 3: Regresar a la casa a las 14:30 y descansar.\n")

# Cerramos el archivo después de escribir para guardar los cambios
archivo.close()

# 2. Lectura de Archivo de Texto
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos el contenido línea por línea usando readline()
linea = archivo.readline()  # Leemos la primera línea
while linea != "":          # Mientras no sea el final del archivo
    print(linea, end="")   # Mostramos la línea en consola, end="" evita doble salto de línea
    linea = archivo.readline()  # Leemos la siguiente línea

# Cerramos el archivo después de leer
archivo.close()
