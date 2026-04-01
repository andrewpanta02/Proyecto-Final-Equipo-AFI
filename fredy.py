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