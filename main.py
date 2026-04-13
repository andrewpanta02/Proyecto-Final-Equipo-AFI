import datetime
import random
import time

# --- CLASE DE COLORES (ANSI) ---
class Color:
    VERDE = '\033[92m'      # Remitente / Envío / País / Monto
    CELESTE = '\033[96m'    # Destinatario / Recepción / Opciones
    BLANCO = '\033[0m'      # Instrucciones / Etiquetas
    BOLD = '\033[1m'

def ejecutar_afi():
    # Títulos principales en blanco
    print(f"{Color.BOLD}" + "="*65)
    print("      --- BIENVENIDO A AFI ---    ")
    print("      Sistema de Envío de Remesas - USA     ")
    print("="*65 + f"{Color.BLANCO}\n")

    # --- SECCIÓN REMITENTE (VERDE) ---
    print(f"{Color.VERDE}{Color.BOLD}--- DATOS DE ENVÍO ---{Color.BLANCO}")
    
    while True:
        # Forzamos que el icono sea verde y el texto de la etiqueta vuelva a blanco
        nombre_remitente = input(f"{Color.VERDE}👤{Color.BLANCO} Nombre del remitente: {Color.VERDE}").strip().title()
        print(f"{Color.BLANCO}", end="")
        if nombre_remitente: break
        print("⚠️ Error: El nombre es obligatorio.")
    
    while True:
        tel_remitente = input(f"📞 Teléfono del remitente: {Color.VERDE}").strip()
        print(f"{Color.BLANCO}", end="")
        if tel_remitente.isdigit() and len(tel_remitente) >= 8: break
        print("⚠️ Error: Ingrese un teléfono válido.")

    # 2. PAÍS Y MONTO (Verde)
    paises_validos = ["Mexico", "Colombia", "España", "Guatemala"]
    while True:
        print(f"\n🌍 Países disponibles: {', '.join(paises_validos)}")
        pais_destino = input(f"Seleccione el país de destino: {Color.VERDE}").strip().capitalize()
        print(f"{Color.BLANCO}", end="")
        if pais_destino in paises_validos: break
        print(f"⚠️ Error: '{pais_destino}' no está disponible.")

    while True:
        try:
            monto_input = input(f"\n💵 Monto a enviar (USD): {Color.VERDE}").strip()
            print(f"{Color.BLANCO}", end="")
            monto_usd = float(monto_input)
            if monto_usd > 0: break
            print("⚠️ Error: El monto debe ser positivo.")
        except ValueError:
            print("⚠️ Error: Ingrese un valor numérico.")

    # Cálculos
    tasas = {"Mexico": 17.10, "Colombia": 3920.0, "Guatemala": 7.80, "España": 0.92}
    tasa_aplicada = tasas[pais_destino]
    monto_convertido = monto_usd * tasa_aplicada
    
    print(f"\n{Color.BOLD}💰 Cotización:{Color.BLANCO}")
    print(f"Tasa: 1 USD = {tasa_aplicada} {pais_destino}")
    print(f"Recibirán: {Color.CELESTE}{monto_convertido:,.2f} {pais_destino}{Color.BLANCO}")

    # --- SECCIÓN DESTINATARIO (CELESTE) ---
    print(f"\n{Color.CELESTE}{Color.BOLD}--- DATOS DE RECEPCIÓN ---{Color.BLANCO}")
    
    while True:
        # Forzamos que el icono sea celeste y el texto de la etiqueta vuelva a blanco
        nombre_destinatario = input(f"{Color.CELESTE}👤{Color.BLANCO} Nombre del destinatario: {Color.CELESTE}").strip().title()
        print(f"{Color.BLANCO}", end="")
        if nombre_destinatario: break
        print("⚠️ Error: El nombre es necesario.")

    while True:
        tel_destinatario = input(f"📞 Teléfono del destinatario: {Color.CELESTE}").strip()
        print(f"{Color.BLANCO}", end="")
        if tel_destinatario.isdigit() and len(tel_destinatario) >= 8: break
        print("⚠️ Error: Teléfono inválido.")

    # 5. UBICACIÓN (Celeste)
    print(f"📍 Ubicación en {pais_destino}:")
    region = input(f"   Estado/Depto: {Color.CELESTE}").strip().title()
    print(f"{Color.BLANCO}", end="")
    localidad = input(f"   Municipio/Ciudad: {Color.CELESTE}").strip().title()
    print(f"{Color.BLANCO}", end="")

    # 6. MÉTODO DE PAGO
    nombre_banco = "N/A"
    numero_cuenta = "N/A"
    while True:
        print(f"\n¿Cómo recibirá el dinero {nombre_destinatario}?")
        print("1. Efectivo (Ventanilla)")
        print("2. Depósito Bancario")
        opcion = input(f"Opción: {Color.CELESTE}").strip()
        print(f"{Color.BLANCO}", end="")
        
        if opcion == "1":
            metodo_pago = "Efectivo (Ventanilla)"
            break
        elif opcion == "2":
            metodo_pago = "Depósito Bancario"
            nombre_banco = input(f"   Nombre del banco: {Color.CELESTE}").strip().upper()
            print(f"{Color.BLANCO}", end="")
            numero_cuenta = input(f"   Número de cuenta: {Color.CELESTE}").strip()
            print(f"{Color.BLANCO}", end="")
            break
        else:
            print("⚠️ Error: Elija 1 o 2.")

    # Cálculos finales
    costo_servicio = (monto_usd * 0.03) + 5.00
    total_a_pagar = monto_usd + costo_servicio
    id_transaccion = f"AFI-{random.randint(100000, 999999)}"
    fecha_actual = datetime.datetime.now()

    # --- RECIBO FINAL ---
    print("\n" + f"{Color.BOLD}" + "⭐"*22 + " RECIBO AFI " + "⭐"*22)
    print(f"ID Registro: {id_transaccion}")
    print(f"Fecha:       {fecha_actual.strftime('%d/%m/%Y %H:%M')}")
    print("-" * 55)
    
    print(f"REMITENTE:")
    print(f"Nombre:      {Color.VERDE}{nombre_remitente}{Color.BLANCO}")
    print(f"Teléfono:    {Color.VERDE}{tel_remitente}{Color.BLANCO}")
    print("-" * 55)
    
    print(f"DESTINATARIO:")
    print(f"Nombre:      {Color.CELESTE}{nombre_destinatario}{Color.BLANCO}")
    print(f"Teléfono:    {Color.CELESTE}{tel_destinatario}{Color.BLANCO}")
    print(f"Ubicación:   {Color.CELESTE}{localidad}, {region}, {pais_destino}{Color.BLANCO}")
    print(f"Método Pago: {Color.CELESTE}{metodo_pago}{Color.BLANCO}")
    
    if metodo_pago == "Depósito Bancario":
        print(f"Banco:       {Color.CELESTE}{nombre_banco}{Color.BLANCO}")
        print(f"No. Cuenta:  {Color.CELESTE}{numero_cuenta}{Color.BLANCO}")
        
    print("-" * 55)
    print(f"Monto Principal:      ${monto_usd:,.2f} USD")
    print(f"Monto a Recibir:      {Color.CELESTE}{monto_convertido:,.2f} {pais_destino}{Color.BLANCO}")
    print(f"Costo de Servicio:    ${costo_servicio:,.2f} USD")
    print("-" * 55)
    print(f"TOTAL DEBITADO:       {Color.BOLD}${total_a_pagar:,.2f} USD{Color.BLANCO}")
    print("="*56 + f"{Color.BLANCO}")

if __name__ == "__main__":
    ejecutar_afi()