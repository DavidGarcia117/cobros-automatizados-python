def mensaje(numWhatsapp: int, name: str, correoDestino: str, direccion: str, 
            txtValor: str, deuda: int) -> str:

    # Convertir a mayúsculas el nombre
    name_upper = name.strip().upper()
    deuda_formateada = f"{deuda:,}"

    # Crear el mensaje
    message = (
        f"Señor (a)\n"
        f"{name_upper}\n"
        f"Dir.: {direccion}\n"
        f"Tel: {numWhatsapp}\n"
        f"Email: {correoDestino}\n"
        
        "Buen día.\n\n"
        "Escribe Deiber, Abogado & Jurídico de la empresa SÚPERGIROS CAUCA, "
        f"mediante el presente mensaje se recuerda deuda a su nombre registrada en el sistema de la compañía "
        f"por la suma de {txtValor} M/CTE ($ {deuda_formateada}).\n\n"
        "Así las cosas, y con la finalidad de precaver la iniciación de las acciones legales en su contra, "
        "le hacemos un llamado para que en esta etapa realice abonos o dé inicio a un acuerdo de pago evitando "
        "reportes negativos en centrales de riesgos, demandas, embargos y cobros reiterativos mediante llamadas o correos.\n\n"
        "En caso de realizar abonos, acérquese a un punto principal de SUPERGIROS bajo el concepto 'abono a faltante' "
        "con su número de cédula y espere el soporte de pago.\n\n"
        "Favor enviar soportes de pago a los siguientes medios: prueba@ejemplo.co – Y/O al abonado telefónico 333 111 2222 "
        "– indicando su nombre completo y número de cédula."
    )

    return message
