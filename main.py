def calcular_transferencia(pais_destino, monto_usd):
    import random
    from datetime import datetime

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