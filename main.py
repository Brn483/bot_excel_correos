import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("clientes1.xlsx")

# Recorrer los contactos y generar un mensaje personalizado
for index, row in df.iterrows():
    nombre = row["Nombre"]
    correo = row["Correo"]
    
    mensaje = f"""
    Hola {nombre},

    Este es un mensaje de prueba para ti. 
    Gracias por ser parte de nuestro proyecto. 

    Atentamente,  
    Brayan (bot automático)
    """

    print(f"📧 Enviando a: {correo}")
    print(mensaje)
    print("=" * 40)
