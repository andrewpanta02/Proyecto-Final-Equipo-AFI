import random
from datetime import datetime

def bienvenida():
    print("Bienvenido al programa de envío de remesas a Latinoamérica.\n")
    nombre_remitente = input("Ingrese su nombre completo: ")
    nombre_destinatario = input("Ingrese el nombre completo del destinatario: ")
    pais_destino = input("Ingrese el país de destino (Mexico, Colombia, Peru): ")    
    monto_enviar = float(input("Ingrese el monto a enviar en USD: "))
    
    return nombre_remitente, nombre_destinatario, pais_destino, monto_enviar

def calcular_transferencia(pais_destino, monto_usd):
    # Seleccionar tasa
    if pais_destino == "Mexico":
        tasa = 17.10
    elif pais_destino == "Colombia":
        tasa = 3920.00
    elif pais_destino == "Guatemala":
        tasa = 7.80
    else:
        tasa = 1.0
    
    # Cálculos
    monto_convertido = monto_usd * tasa
    costo_servicio = (monto_usd * 0.03) + 5.00
    total_a_pagar = monto_usd + costo_servicio

    # ID y fecha
    id_transferencia = random.randint(100000, 999999)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return monto_convertido, costo_servicio, total_a_pagar, id_transferencia, fecha

# --- TERCERA PARTE: SALIDA Y ALMACENAMIENTO ---
    print("\n" + "*"*40)
    print("         RESUMEN DE TRANSACCIÓN")
    print("*"*40)
    print(f"ID Transacción:   {id_transferencia}")
    print(f"Fecha:            {fecha_actual.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Remitente:        {nombre_remitente}")
    print(f"País Destino:     {pais_destino}")
    print("-" * 40)
    print(f"Monto a enviar:   ${monto_usd:,.2f} USD")
    print(f"Monto a recibir:  {monto_convertido:,.2f} ({pais_destino})")
    print(f"Costo de envío:   ${costo_servicio:,.2f} USD")
    print("-" * 40)
    print(f"TOTAL DEBITADO:   ${total_a_pagar:,.2f} USD")
    print("*"*40)

 # Guardado en archivo LOG
    try:
        with open("log_transferencias.txt", "a", encoding="utf-8") as log:
            log.write(f"\n--- REGISTRO {id_transferencia} ---\n")
            log.write(f"Fecha: {fecha_actual}\n")
            log.write(f"Remitente: {nombre_remitente} | Destino: {pais_destino}\n")
            log.write(f"Monto USD: ${monto_usd} | Total Pagado: ${total_a_pagar}\n")
            log.write("-" * 30 + "\n")
        print("\n✅ Registro guardado exitosamente en log_transferencias.txt")
    except IOError:
        print("\n❌ Error crítico: No se pudo escribir en el archivo de registro.")

    print("\nGracias por confiar en AFI. ¡Feliz día!")

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_afi() 