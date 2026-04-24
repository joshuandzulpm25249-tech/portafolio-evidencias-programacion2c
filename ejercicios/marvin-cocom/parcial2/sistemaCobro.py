#PROGRAMA DE GESTIÓN DE VENTAS (MODULARIZADO)
# Calcula subtotal, descuento, IVA y #total a pagar

# -------- FUNCIONES (MÓDULOS) --------

# Función para calcular subtotal
def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal multiplicando precio por cantidad.
    Parámetros: precio, cantidad
    Retorna: subtotal
    """
    subtotal = precio * cantidad
    return subtotal


# Función para calcular descuento
def calcular_descuento(subtotal):
    """
    Aplica descuento del 10% si el subtotal es mayor a 1000.
    Parámetros: subtotal
    Retorna: descuento
    """
    if subtotal > 1000:
        descuento = subtotal * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento}")
    else:
        descuento = 0
    return descuento


# Función para calcular IVA
def calcular_iva(subtotal_con_descuento):
    """
    Calcula el IVA del 16%.
    Parámetros: subtotal con descuento
    Retorna: iva
    """
    iva = subtotal_con_descuento * 0.16
    return iva


# Función para mostrar ticket
def mostrar_ticket(producto, subtotal, iva, total_final):
    """
    Muestra los datos finales en pantalla.
    Parámetros: producto, subtotal, iva, total
    """

    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("------------------------")


# -------- FLUJO PRINCIPAL DEL PROGRAMA --------
def main():
    print("--- Sistema de Cobro v1.0 ---")

    # Entrada de datos
    producto = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    # Cálculos usando funciones
    subtotal = calcular_subtotal(precio, cantidad)

    descuento = calcular_descuento(subtotal)

    subtotal_con_descuento = subtotal - descuento

    iva = calcular_iva(subtotal_con_descuento)

    total_final = subtotal_con_descuento + iva

    # Mostrar resultados
    mostrar_ticket(producto, subtotal, iva, total_final)

if __name__ == "__main__":
    main()
