def bienvenida():
    print("Bienvenido al programa de envío de remesas a Latinoamérica.\n")
    nombre_remitente = input("Ingrese su nombre completo: ")
    nombre_destinatario = input("Ingrese el nombre completo del destinatario: ")
    pais_destino = input("Ingrese el país de destino (Mexico, Colombia, Peru): ")    
    monto_enviar = float(input("Ingrese el monto a enviar en USD: "))
    
    return nombre_remitente, nombre_destinatario, pais_destino, monto_enviar

# Función para determinar el tipo de cambio
def validar_if(pais_destino):
    if pais_destino == "Mexico":
        return 20.5
    elif pais_destino == "Colombia":
        return 3800.0
    elif pais_destino == "Peru":
        return 3.5
    else:
        return None
#
# --- INICIO DEL PROGRAMA ---

# 1. Llamamos a la función y guardamos los datos en variables
nom_rem, nom_dest, pais, monto = bienvenida()

# 2. Obtenemos el tipo de cambio según el país ingresado
t_cambio = validar_if(pais)

# 3. Verificamos si el país fue válido y calculamos
if t_cambio is not None:
    monto_final = monto * t_cambio
    print("\n" + "="*30)
    print(f"RESUMEN DE ENVÍO")
    print(f"Remitente: {nom_rem}")
    print(f"Destinatario: {nom_dest}")
    print(f"Destino: {pais}")
    print(f"Monto enviado: ${monto} USD")
    print(f"Tipo de cambio: {t_cambio}")
    print("-" * 30)
    # Aquí imprimimos el monto convertido
    print(f"TOTAL A RECIBIR: {monto_final} en moneda local.")
    print("="*30)
else:
    print("Error: El país ingresado no está en nuestra base de datos.")
