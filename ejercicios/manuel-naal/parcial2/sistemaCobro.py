#Funciones(Modulo)

def d(Subtotal, porcentaje):
    """
    Calcula el monto de dinero a descontar.
    Multiplica el subtotal por el porcentaje (ej. 15) dividido entre 100.

    Argumentos:
        Subtotal (float): Monto total antes del descuento.
        Porcentaje (float): Porcentaje de descuento que se debe aplicar.

    Retorno:
        (float): Cantidad de dinero que se descontara.
    """
    return Subtotal * (porcentaje/ 100)

def calcular_iva(sub_con_descuento, tasa):
    """
    Calcular el IVA sobre el monto que ya tiene el descuento aplicado.

    Argurmentos:
        sub_con_descuentos (float): Subtotal de venta.
        tasa (float): POrcentaje de descuento aplicable.

    Retorno:
        (float): Monto del iva de la venta.
    """
    return sub_con_descuento * tasa 

# --- PROGRAMA PRINCIPAL ---

def main():
    #1. Inicio del programa y captura de datos
    print("-- Ticket de ventas --")

    #Convertimos las entradas a float para poder hacer calculos 
    sub_inicial = float(input("Ingrese el subtotal de la compra: "))
    por_descuento = float(input("Ingrese el porcentaje de descuento: "))
    porcentaje_iva = 0.16
    #2. Procesamiento de la informacion usando las funciones 
    #calculamos cuanto se descuenta
    monto_descuento = d(sub_inicial, por_descuento)

    #Obtenemos el nuevo subtotal restando el descuento
    sub_con_descuento = sub_inicial - monto_descuento
    
    #Calculamos IVA sobre el nuevo subtotal
    monto_iva = calcular_iva(sub_con_descuento, porcentaje_iva)

    #Sumamoes el subtotal rebajado mas el IVA para el total
    total_final = sub_con_descuento + monto_iva    

    if __name__ == "__main__":
        main()