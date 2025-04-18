# import scan_ports  # Removed as it cannot be resolved
import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return port, True
    except:
        return port, False

def run_port_scan(target, ports=range(1, 1025), threads=100):
    print(f"[🔍] Scansione porte su {target}...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)

    for port, status in results:
        if status:
            print(f"[✅] Porta {port} è aperta.")
            open_ports.append(port)

    if not open_ports:
        print("❌ Nessuna porta aperta trovata.")
    else:
        print(f"[✔️] Porte aperte trovate: {open_ports}")
    return open_ports
