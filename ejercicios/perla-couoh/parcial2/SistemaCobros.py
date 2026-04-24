# --- FUNCIONES (Módulos) ---

# -------- FUNCIONES DE CÁLCULO --------

def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal multiplicando el precio por la cantidad.
    
    Parámetros:
    precio (float): precio unitario del producto
    cantidad (int): cantidad comprada
    
    Retorna:
    float: subtotal de la compra
    """
    return precio * cantidad


def calcular_descuento(subtotal):
    """
    Aplica un descuento del 10% si el subtotal es mayor a 1000.
    
    Parámetros:
    subtotal (float): total sin descuento
    
    Retorna:
    float: monto del descuento aplicado
    """
    if subtotal > 1000:
        descuento = subtotal * 0.10
        print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")
        return descuento
    return 0


def calcular_iva(subtotal_con_descuento):
    """
    Calcula el IVA del 16%.
    
    Parámetros:
    subtotal_con_descuento (float): subtotal después del descuento
    
    Retorna:
    float: IVA calculado
    """
    return subtotal_con_descuento * 0.16


def calcular_total(subtotal_con_descuento, iva):
    """
    Calcula el total final sumando subtotal con descuento e IVA.
    
    Parámetros:
    subtotal_con_descuento (float)
    iva (float)
    
    Retorna:
    float: total a pagar
    """
    return subtotal_con_descuento + iva


# -------- FUNCIÓN DE SALIDA --------

def imprimir_ticket(producto, subtotal, iva, total):
    """
    Imprime el ticket de compra en pantalla.
    
    Parámetros:
    producto (str): nombre del producto
    subtotal (float)
    iva (float)
    total (float)
    
    Retorna:
    None
    """
    print("\n--- TICKET DE VENTA ---")
    print(f"Producto: {producto}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("----------------------")


# -------- FUNCIÓN QUE REALIZA UN COBRO --------

def realizar_cobro():
    """
    Ejecuta todo el proceso de un cobro:
    - Solicita datos al usuario
    - Realiza cálculos
    - Muestra el ticket
    
    Retorna:
    None
    """
    producto = input("\nNombre del producto: ")
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))

    subtotal = calcular_subtotal(precio, cantidad)
    descuento = calcular_descuento(subtotal)
    subtotal_con_descuento = subtotal - descuento
    iva = calcular_iva(subtotal_con_descuento)
    total = calcular_total(subtotal_con_descuento, iva)

    imprimir_ticket(producto, subtotal, iva, total)


# -------- FUNCIÓN PRINCIPAL --------

def main():
    """
    Controla el flujo del programa completo.
    Permite realizar múltiples cobros sin repetir código.
    """
    print("--- Sistema de Cobro v2.0 ---")

    while True:
        realizar_cobro()  # Llama al proceso completo

        # Pregunta al usuario si desea continuar
        opcion = input("\n¿Deseas realizar otro cobro? (s/n): ").lower()
        if opcion != 's':
            print("Gracias por usar el sistema.")
            break


# -------- EJECUCIÓN DEL PROGRAMA --------

if __name__ == "__main__":
    main()
