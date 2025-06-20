from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import util.Recordatorio as r
import os

def obtener_fecha() -> str:
    now = datetime.now()
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = str(now.day)
    month = str(months[now.month - 1])
    year = str(now.year)
    return f"{day} de {month} de {year}"

def enviarCorreo(correoDestino: str, correoCopia: str, correoOrigen: str, contra: str, 
                 numWhatsapp: int, name: str, direccion: str, txtValor: str, deuda: int) -> None:
    
    try:
        # Crear el mensaje
        msg = MIMEMultipart()
        message = r.mensaje(numWhatsapp, name, correoDestino, direccion, txtValor, deuda)

        # Estructura del correo
        password = ("Casio2025*")  # Usar variable de entorno, si está disponible
        msg['From'] = correoOrigen
        msg['To'] = correoDestino
        msg['Cc'] = correoCopia
        msg['Subject'] = f"SOLICITUD DE PAGO {datetime.now().date()}"  # Asunto del correo
        tocc = correoCopia.split(",") + [correoDestino]

        # Agregar el cuerpo del mensaje
        msg.attach(MIMEText(message, 'plain'))

        # Instanciar servidor
        with smtplib.SMTP('correo.supergiroscauca.co', 587) as server:
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], tocc, msg.as_string())

        print(f"Envio de Correo exitoso a {msg['To']}")

    except Exception as e:
        print(f"Error al enviar correo a {correoDestino}: {str(e)}")
