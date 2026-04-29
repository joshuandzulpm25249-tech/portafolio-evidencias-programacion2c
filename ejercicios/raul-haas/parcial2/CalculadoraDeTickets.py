#Raul Haas Pool

def calcular_subtotal(precio, cantidad):
    """
    Calcula el subtotal de una compra multiplicando precio por cantidad.
    
    Argumentos:
        precio (float): Precio unitario del producto.
        cantidad (int): Cantidad de productos a comprar.
        
    Retorno:
        (float): El subtotal sin descuentos ni impuestos.
    """
    subtotal = precio * cantidad
    return subtotal

def calcular_descuento(subtotal, porcentaje_descuento):
    """
    Calcula el monto en dinero que se descuenta del subtotal.
    
    Argumentos:
        subtotal (float): Monto base sobre el que se aplica el descuento.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar.
        
    Retorno:
        (float): El monto en pesos del descuento calculado.
    """
    descuento = subtotal * porcentaje_descuento / 100
    return descuento

def subtotal_con_descuento(subtotal, descuento):
    """
    Resta el monto del descuento al subtotal original.
    
    Argumentos:
        subtotal (float): Subtotal antes de aplicar descuento.
        descuento (float): Monto en pesos que se va a descontar.
        
    Retorno:
        (float): Nuevo subtotal ya con el descuento aplicado.
    """
    subtotal_descontado = subtotal - descuento
    return subtotal_descontado

def calcular_iva(subtotal_descontado, porcentaje_iva):
    """
    Calcula el monto del IVA sobre el subtotal con descuento.
    
    Argumentos:
        subtotal_descontado (float): Monto base para calcular el impuesto.
        porcentaje_iva (float): Porcentaje de IVA a aplicar.
        
    Retorno:
        (float): El monto en pesos del IVA calculado.
    """
    iva = subtotal_descontado * porcentaje_iva / 100
    return iva

def calcular_total(subtotal_descontado, iva):
    """
    Calcula el total final sumando el subtotal con descuento más el IVA.
    
    Argumentos:
        subtotal_descontado (float): Subtotal después del descuento.
        iva (float): Monto del impuesto calculado.
        
    Retorno:
        (float): El total final a pagar por el cliente.
    """
    total = subtotal_descontado + iva
    return total

def mostrar_ticket(precio, cantidad, desc_porc, iva_porc):
    """
    Orquesta todas las funciones de cálculo e imprime el ticket de compra.
    
    Argumentos:
        precio (float): Precio unitario del producto ingresado por el usuario.
        cantidad (int): Cantidad de productos ingresada por el usuario.
        desc_porc (float): Porcentaje de descuento ingresado por el usuario.
        iva_porc (float): Porcentaje de IVA ingresado por el usuario.
        
    Retorno:
        None: Esta función no retorna valor, solo imprime el ticket en pantalla.
    """
    sub = calcular_subtotal(precio, cantidad)
    desc_monto = calcular_descuento(sub, desc_porc)
    sub_desc = subtotal_con_descuento(sub, desc_monto)
    iva_monto = calcular_iva(sub_desc, iva_porc)
    total_final = calcular_total(sub_desc, iva_monto)
    
    print("\n--- TICKET DE COMPRA ---")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: ${sub}")
    print(f"Descuento {desc_porc}%: -${desc_monto}")
    print(f"Subtotal con descuento: ${sub_desc}")
    print(f"IVA {iva_porc}%: +${iva_monto}")
    print(f"TOTAL A PAGAR: ${total_final}")
    print("------------------------\n")

def main():
    while True:
        print("=== MENÚ SISTEMA DE COBRO ===")
        print("1. Calcular nuevo ticket")
        print("2. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                precio = float(input("Ingresa el precio del producto: $"))
                cantidad = int(input("Ingresa la cantidad: "))
                desc = float(input("Ingresa el % de descuento: "))
                iva = float(input("Ingresa el % de IVA: "))
                
                mostrar_ticket(precio, cantidad, desc, iva)
                
            except ValueError:
                print("Error: Ingresa solo números. Intenta de nuevo.\n")
                
        elif opcion == "2":
            print("Saliendo del sistema. ¡Gracias!")
            break
        else:
            print("Opción inválida. Elige 1 o 2.\n")

# Iniciar el programa
if __name__ == "__main__":
    main()
