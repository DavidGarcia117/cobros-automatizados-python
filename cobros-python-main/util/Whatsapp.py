import pyautogui as pg
import webbrowser as web
import time as t
import pyperclip as ppc
import util.Recordatorio as r

def enviarWhatsapp(numWhatsapp: int, name: str, correoDestino: str, direccion: str, 
                   txtValor: str, deuda: int) -> None:

    try:
        # Generar el mensaje usando la función de Recordatorio
        message = r.mensaje(numWhatsapp, name, correoDestino, direccion, txtValor, deuda)

        # Validar y formatear el número de WhatsApp
        numWhatsapp = str(numWhatsapp).strip()
        if len(numWhatsapp) != 10 or not numWhatsapp.isdigit():
            print(f"El número de WhatsApp {numWhatsapp} no es válido.")
            return
        
        # Formatear el número de teléfono con el código del país (+57)
        phone_no = f"+57{numWhatsapp}"

        # URL de WhatsApp Web con el mensaje
        url = f"https://web.whatsapp.com/send?phone={phone_no}"
        
        # Abrir una ventana en el navegador
        web.open(url)
        t.sleep(12)  # Esperar a que la página cargue completamente (ajustar si es necesario)
        
        # Copiar el mensaje al portapapeles y pegarlo en WhatsApp Web
        ppc.copy(message)
        pg.hotkey('ctrl', 'v')
        t.sleep(6)  # Dar tiempo para pegar el mensaje
        
        # Presionar Enter para enviar el mensaje
        pg.press('enter')
        t.sleep(5)  # Esperar un momento antes de cerrar la pestaña
        
        # Cerrar la pestaña del navegador
        pg.hotkey('ctrl', 'w')
        t.sleep(2)

        print(f"Mensaje enviado a {name} ({phone_no}) con éxito.")

    except Exception as e:
        print(f"Error al enviar mensaje a {numWhatsapp}: {str(e)}")
