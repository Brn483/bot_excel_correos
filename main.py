import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os



# Cargar el archivo Excel
df = pd.read_excel("clientes1.xlsx")

# Configura tu correo de prueba
load_dotenv()

correo_emisor = os.getenv("EMAIL")
clave_aplicacion = os.getenv("CLAVE_APP")
#crea un archivo .env en la raiz y ahi pon tus datos reales de correo:
# EMAIL=miemail@example.com 
# CLAVE_APP=miclaveapp1234


# Inicia el servidor SMTP de Gmail
servidor = smtplib.SMTP("smtp.gmail.com", 587)
servidor.starttls()
servidor.login(correo_emisor, clave_aplicacion)

# Recorrer cada contacto
for index, row in df.iterrows():
    nombre = row["Nombre"]
    correo_destino = row["Correo"]
    
    asunto = "Hola desde Python 👋"
    cuerpo = f"""
    Hola {nombre},

    Este es un mensaje enviado automáticamente desde un bot en Python.
    ¡Gracias por participar en este proyecto de prueba!

    Saludos,  
    Brayan Villanueva
    """

    # Armar el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = correo_emisor
    mensaje["To"] = correo_destino
    mensaje["Subject"] = asunto

    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Enviar el correo
    servidor.sendmail(correo_emisor, correo_destino, mensaje.as_string())
    print(f"📬 Correo enviado a {correo_destino}")

# Cerrar conexión
servidor.quit()
print("✅ Todos los correos fueron enviados.")