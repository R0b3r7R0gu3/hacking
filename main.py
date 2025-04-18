import os
import sys
import subprocess
import time

# Funzioni per ciascun tool
def phishing_attack():
    print("Avvio phishing server...")
    try:
        from modules.social_engineering.phishing_attack import start_phishing_server
        start_phishing_server()
    except ImportError as e:
        print(f"Errore nell'importazione del phishing: {e}")

def port_scanner():
    print("Avvio Port Scanner...")
    try:
        from modules.network.port_scanner import scan_ports
        scan_ports()
    except ImportError as e:
        print(f"Errore nell'importazione del Port Scanner: {e}")

def ftp_brute_force(host="127.0.0.1", port=21, users=["admin", "user"], passwords=["password", "1234"]):
    print("Avvio FTP Brute Force...")
    try:
        from modules.automation.brute_force import ftp_bruteforce
        ftp_bruteforce()
    except ImportError as e:
        print(f"Errore nell'importazione del Brute Force FTP: {e}")

def network_sniffer():
    print("Avvio Network Sniffer...")
    try:
        from modules.network.sniffer import start_sniffer
        start_sniffer()
    except ImportError as e:
        print(f"Errore nell'importazione del Network Sniffer: {e}")

def automatic_attack():
    print("Avvio Attacco Automatico...")
    try:
        from modules.automation.auto_attack import start_attack
        start_attack()
    except ImportError as e:
        print(f"Errore nell'importazione dell'attacco automatico: {e}")

def keylogger_python():
    print("Avvio Keylogger Python...")
    try:
        from modules.social_engineering.keylogger import start_keylogger
        start_keylogger()
    except ImportError as e:
        print(f"Errore nell'importazione del keylogger: {e}")

import platform

def access_remoto():
    if platform.system() != "Windows":
        print("Accesso remoto supportato solo su Windows.")
        return
    os.system("powershell access_remoto.ps1")
    print("Avvio Accesso Remoto...")
    try:
        from modules.remote_access.access_remoto import start_remote_access
        start_remote_access()
        subprocess.run(["powershell", "-ExecutionPolicy", "ByPass", "-File", "modules/access_remoto.ps1"])
    except Exception as e:
        print(f"Errore nell'esecuzione dell'accesso remoto: {e}")

def privilege_escalation():
    print("Avvio Privilege Escalation...")
    try:
        from modules.post_exploitation.privilege_escalation import escalate_privileges
        escalate_privileges()
    except ImportError as e:
        print(f"Errore nell'importazione della Privilege Escalation: {e}")

def exploit_execution():
    print("Esecuzione Exploit...")
    try:
        from modules.exploits.run_exploit import execute_exploit
        execute_exploit()
    except ImportError as e:
        print(f"Errore nell'esecuzione dell'exploit: {e}")

def exit_program():
    print("Uscita dal programma...")
    sys.exit(0)

# Funzione per il menu principale
def main_menu():
    menu = """
    ------------------------
    |  Hacking Tool Menu    |
    ------------------------
    1. Phishing Server
    2. Port Scanner
    3. FTP Brute Force
    4. Network Sniffer
    5. Attacco Automatico
    6. Keylogger Python
    7. Accesso Remoto
    8. Privilege Escalation
    9. Exploit Execution
    0. Exit
    ------------------------
    Seleziona un'opzione:
    """

    while True:
        print(menu)
        choice = input("Scegli un'opzione: ")

        if choice == '1':
            phishing_attack()
        elif choice == '2':
            port_scanner()
        elif choice == '3':
            ftp_brute_force()
        elif choice == '4':
            network_sniffer()
        elif choice == '5':
            automatic_attack()
        elif choice == '6':
            keylogger_python()
        elif choice == '7':
            access_remoto()
        elif choice == '8':
            privilege_escalation()
        elif choice == '9':
            exploit_execution()
        elif choice == '0':
            exit_program()
        else:
            print("Opzione non valida. Riprova.")

# Esegui il menu principale
if __name__ == "__main__":
    main_menu()
