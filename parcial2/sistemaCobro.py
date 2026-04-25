
# --- FUNCIONES (Módulos) ---

def calcular_descuento(subtotal):
    """Calcula un 10% de descuento si el monto supera los 1000."""
    if subtotal > 1000:
        return subtotal * 0.10
    return 0

def calcular_iva(monto):
    """Calcula el IVA del 16% sobre un monto dado."""
    return monto * 0.16

def imprimir_ticket(producto, subtotal, descuento, iva, total_final):
    """Muestra el desglose de la venta en consola."""
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    if descuento > 0:
        print(f"Descuento (10%): -${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
    print("-----------------------")

# --- FUNCIÓN PRINCIPAL ---

def main():
    print("--- Sistema de Cobro v1.2 (Con función Main) ---")

    # 1. Entrada de datos
    producto = input("Nombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    # 2. Procesamiento (Lógica de negocio)
    subtotal_inicial = precio * cantidad
    monto_descuento = calcular_descuento(subtotal_inicial)
    nuevo_subtotal = subtotal_inicial - monto_descuento
    monto_iva = calcular_iva(nuevo_subtotal)
    total = nuevo_subtotal + monto_iva

    # 3. Salida de resultados
    imprimir_ticket(producto, subtotal_inicial, monto_descuento, monto_iva, total)

# El punto de entrada oficial del programa
if __name__ == "__main__":
    main()
