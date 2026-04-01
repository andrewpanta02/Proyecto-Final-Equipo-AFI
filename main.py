"""
estad
"""

import random
from datetime import datetime
#Esta funcion es la que se encarga de ejecutar todo el programa, desde la bienvenida
def bienvenida():
    print("Bienvenido al programa de envío de remesas a Latinoamérica.\n")
    nombre_remitente = input("Ingrese su nombre completo: ")
    nombre_destinatario = input("Ingrese el nombre completo del destinatario: ")
    pais_destino = input("Ingrese el país de destino (Mexico, Colombia, Peru): ")    
    monto_enviar = float(input("Ingrese el monto a enviar en USD: "))
    
    return nombre_remitente, nombre_destinatario, pais_destino, monto_enviar
    
def calcular_monto(pais_destino, monto_usd):
    #Funcion para calcular el monto a mandar dependiendo de cada pais con un if 
    # Seleccionar tasa
    if pais_destino == "Mexico":
        tasa = 17.10
    elif pais_destino == "Colombia":
        tasa = 3920.00
    elif pais_destino == "Guatemala":
        tasa = 7.80
    else:
        tasa = 1.0
    
    # Cálcula la tasa de cada pais que se ingreso para calcular el monto que se envia
    monto_convertido = monto_usd * tasa
    costo_servicio = (monto_usd * 0.03) + 5.00
    total_a_pagar = monto_usd + costo_servicio

    # esta es para saber la fecha en que se envio y genera un id para el usuario
    id_transferencia = random.randint(100000, 999999)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return monto_convertido, costo_servicio, total_a_pagar, id_transferencia, fecha
def ejecutar_afi():
    #aca lo que imprime en pantalla el resumen de la transaccion con los datos que se ingresaron y los calculos que se hicieron
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

 #Aqui se guarda el registro de la transaccion en un archivo de texto para llevar un control de las transferencias realizadas, si no se puede escribir en el archivo se muestra un mensaje de error.
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

#Y esto es para ejecutar el programa, llamando a la funcion de bienvenida y luego a la funcion de calculos y resumen de la transaccion
if __name__ == "__main__":
    bienvenida() 
    #calcular_monto()
    ejecutar_afi()