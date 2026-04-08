import datetime
import random
import time

# --- CONSTANTES ---
COMISION_FIJA = 5.00
IMPUESTO_TRANSACCION = 0.03

def ejecutar_afi():
    print("========================================")
    print("      --- BIENVENIDO A AFI ---    ")
    print("      Configuración: Estados Unidos     ")
    print("========================================\n")

    # --- PRIMERA PARTE: ENTRADA Y VALIDACIÓN ---
    while True:
        nombre_remitente = input("Ingrese el nombre del remitente: ").strip()
        if not nombre_remitente:
            print("Error: El nombre es obligatorio.")
        else:
            break

    print("\nPaíses disponibles: Mexico, Colombia, España, Guatemala")
    pais_destino = input("Ingrese el país de destino: ").capitalize().strip()

    while True:
        try:
            monto_usd = float(input("Ingrese el monto a enviar (USD): "))
            if monto_usd > 0:
                break
            else:
                print("Error: El monto debe ser un número positivo.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

    # --- SEGUNDA PARTE: LÓGICA Y CÁLCULOS ---
    print("\nProcesando cálculos financieros...")
    time.sleep(1) # Simulación de procesamiento

    # Selección de tasa según país
    if pais_destino == "Mexico":
        tasa = 17.10
    elif pais_destino == "Colombia":
        tasa = 3920.00
    elif pais_destino == "Guatemala":
        tasa = 7.80
    else:
        tasa = 1.0  # Caso para España o países en USD
        print("Nota: Se aplicará tasa 1:1 o moneda base.")

    # Operaciones Matemáticas
    monto_convertido = monto_usd * tasa
    costo_servicio = (monto_usd * IMPUESTO_TRANSACCION) + COMISION_FIJA
    total_a_pagar = monto_usd + costo_servicio
    
    # Generación de metadatos
    id_transferencia = f"AFI-{random.randint(100000, 999999)}"
    fecha_actual = datetime.datetime.now()

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
        print("\n Registro guardado exitosamente en log_transferencias.txt")
    except IOError:
        print("\n Error crítico: No se pudo escribir en el archivo de registro.")

    print("\nGracias por confiar en AFI. ¡Feliz día!")

# Ejecución del programa
if __name__ == "__main__":
    ejecutar_afi() 