import socket

def start_sniffer():
    print("📡 Avvio dello sniffer in corso...")
    try:
        # RAW socket per intercettare i pacchetti
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        s.bind(("0.0.0.0", 0))
        s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        while True:
            packet = s.recvfrom(65565)
            print(f"[📦] Pacchetto ricevuto: {packet[0][:20]}...")

    except Exception as e:
        print(f"[❌] Errore sniffer: {e}")
    finally:
        try:
            s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except:
            pass
