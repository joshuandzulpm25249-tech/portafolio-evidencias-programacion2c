# --- FUNCIONES ---

def calcular_descuento(subtotal, porcentaje):
    """
    Calcula el monto de dinero a descontar basado en un subtotal y un porcentaje.
    
    Args:
        subtotal (float): El monto inicial de la compra.
        porcentaje (float): El valor del descuento (ej. 15 para 15%).
        
    Returns:
        float: El monto total a restar del subtotal inicial.
    """
    return subtotal * (porcentaje / 100)

def calcular_iva(sub_con_descuento, tasa):
    """
    Calcula el impuesto (IVA) sobre el monto que ya tiene el descuento aplicado.
    
    Args:
        sub_con_descuento (float): El subtotal después de aplicar descuentos.
        tasa (float): El factor del impuesto (ej. 0.16 para 16%).
        
    Returns:
        float: El monto resultante del impuesto.
    """
    return sub_con_descuento * tasa

# --- PROGRAMA PRINCIPAL ---

def main():
    # 1. Inicio del programa y captura de datos
    print("-- Ticket de ventas --")
    
    # Convertimos las entradas a float para poder hacer cálculos
    sub_inicial = float(input("Ingrese el subtotal de la compra: "))
    por_descuento = float(input("Ingrese el porcentaje de descuento: "))
    porcentaje_iva = 0.16
    
    # 2. Procesamiento de la información usando las funciones
    # Calculamos cuánto se descuenta
    monto_descuento = calcular_descuento(sub_inicial, por_descuento)
    
    # Obtenemos el nuevo subtotal restando el descuento
    subtotal_con_descuento = sub_inicial - monto_descuento
    
    # Calculamos el IVA sobre el nuevo subtotal
    monto_iva = calcular_iva(subtotal_con_descuento, porcentaje_iva)
    
    # Sumamos el subtotal rebajado más el IVA para el total
    total_final = subtotal_con_descuento + monto_iva
    
    # 3. Despliegue de resultados (El Ticket)
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"Descuento aplicado: $ {monto_descuento:.2f}")
    print(f"Subtotal neto:      $ {subtotal_con_descuento:.2f}")
    print(f"IVA (16%):          $ {monto_iva:.2f}")
    print(f"TOTAL A PAGAR:      $ {total_final:.2f}")
    print("-------------------------")
    
    # 4. Opción de salir
    input("Presione ENTER para salir...")

# Llamada a la función principal
if __name__ == "__main__":
    main()