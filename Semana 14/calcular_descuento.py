# Definición de la función
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento aplicado al monto total.

    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal

# Primera llamada: usando el valor predeterminado del descuento
monto_compra1 = 150
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print(f"Compra 1:")
print(f"Monto total: ${monto_compra1}")
print(f"Descuento aplicado: ${descuento1}")
print(f"Monto a pagar: ${monto_final1}")
print("---------------------------")

# Segunda llamada: proporcionando un porcentaje de descuento diferente
monto_compra2 = 200
descuento2 = calcular_descuento(monto_compra2, 20)  # 20% de descuento
monto_final2 = monto_compra2 - descuento2

print(f"Compra 2:")
print(f"Monto total: ${monto_compra2}")
print(f"Descuento aplicado: ${descuento2}")
print(f"Monto a pagar: ${monto_final2}")