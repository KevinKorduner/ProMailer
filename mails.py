import pymysql
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configurar la conexión a la base de datos MySQL en XAMPP
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='QUx2611xw',
    database='database'
)
cursor = conn.cursor()

# Obtener los correos electrónicos de la base de datos
cursor.execute("SELECT email FROM users")
emails = cursor.fetchall()

# Configurar el servidor SMTP
smtp_server = 'smtp.server.com'
smtp_port = 587
smtp_user = 'kevin@kevinkorduner.com'
smtp_password = 'Hw1QPKSgPasswordHere!'

# Crear la conexión con el servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_user, smtp_password)

# Configurar el mensaje HTML
subject = "Kicks Online is Back! Double EXP Weekend 🎉"
html_body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kicks Online - We Are Back!</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px; text-align: center; color: #333;">
    <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
        <h1 style="color: #ff5733;">⚽ Kicks Online is Back! 🎮</h1>
        <p style="font-size: 18px;">Dear <strong>Player</strong>,</p>
        <p style="font-size: 18px;">We are excited to announce that <strong>Kicks Online</strong> is back online! 🌐</p>
        <p style="font-size: 18px;">To celebrate, we're kicking off a special event:</p>
        <h2 style="color: #28a745;">🎉 Double EXP Weekend! 🎉</h2>
        <p style="font-size: 18px;">Join us this weekend and earn <strong>Double EXP</strong> in all your matches! It's the perfect time to level up and show off your skills on the field. 🚀</p>
        <p style="font-size: 18px;">Don't miss out on the action – gather your team and let's play some football! 🏆</p>
        <p style="font-size: 18px;">We can't wait to see you back in the game! ⚡</p>

        <p style="font-size: 18px;">
            Join our community on <a href="https://discord.com/invite/9bH9adPBxf" style="color: #7289da; text-decoration: none;"><strong>Discord</strong></a> and stay updated with the latest news! 💬
        </p>

        <a href="https://kicks-online.net/en/game" style="display: inline-block; margin: 10px; padding: 15px 25px; font-size: 16px; font-weight: bold; color: #ffffff; background-color: #ff5733; border-radius: 5px; text-decoration: none;">
            Download Kicks Online 2024
        </a>
        <a href="https://nosetu.com/" style="display: inline-block; margin: 10px; padding: 15px 25px; font-size: 16px; font-weight: bold; color: #ffffff; background-color: #28a745; border-radius: 5px; text-decoration: none;">
            Forum
        </a>

        <p style="font-size: 18px;">Best regards,</p>
        <p style="font-size: 18px;"><strong>KicksOnline.net</strong></p>
    </div>
</body>
</html>
"""

log_id = 1
log_file = open("log.txt", "w")

for email in emails:
    try:
        # Configurar el mensaje MIME
        msg = MIMEMultipart('alternative')
        msg['From'] = smtp_user
        msg['To'] = email[0]
        msg['Subject'] = subject

        # Agregar el cuerpo del correo en HTML
        msg.attach(MIMEText(html_body, 'html'))

        # Enviar el correo
        server.send_message(msg)
        
        # Escribir en el archivo de log
        log_file.write(f"Log ID: {log_id} - Email sent to: {email[0]}\n")
        print(f"Correo enviado a {email[0]}")

        log_id += 1
        
        # Pausar entre envíos para evitar la suspensión del SMTP
        time.sleep(2)  # Pausa de 2 segundos, ajustable si es necesario

    except Exception as e:
        # Manejar errores en el envío del correo
        log_file.write(f"Log ID: {log_id} - Error sending to: {email[0]} - {str(e)}\n")
        print(f"Error enviando a {email[0]}: {str(e)}")
        log_id += 1

# Cerrar la conexión con el servidor SMTP
server.quit()

# Escribir finalización en el archivo de log
log_file.write("Finalizado con éxito!\n")
log_file.close()

# Cerrar la conexión a la base de datos
conn.close()
