# 💻 Ultimate-Hack-Suite

> 🧠 **Ultimate-Hack-Suite** è una suite avanzata di strumenti per ethical hacking e cybersecurity, pensata per offrire un'esperienza completa e potente. Include tool reali e funzionanti, sviluppati in più linguaggi come **Python**, **C** e **PowerShell**, coprendo tutti gli aspetti fondamentali del penetration testing moderno.

---

## 🔥 Caratteristiche principali

Ultimate-Hack-Suite integra una vasta gamma di strumenti professionali per test di sicurezza e auditing:

- 🧠 **Social Engineering**
  - Phishing con pagine web reali (login simulatori)
  - Raccolta credenziali tramite server locale

- 🛠️ **Exploits**
  - Esecuzione exploit C compilabili su sistemi target
  - Privilege escalation per l’ottenimento di privilegi di root/admin

- 🧬 **Keylogger**
  - Completamente silenzioso
  - Salvataggio in file locale (`keylog.txt`)

- 🚪 **Accesso remoto**
  - Reverse shell tramite PowerShell
  - Controllo a distanza e interazione con la shell della vittima

- 🧪 **Brute Force**
  - Password brute force su servizi e dizionari custom
  - Struttura modulare per supportare nuovi target

- 🌐 **Network Attacks**
  - Packet Sniffer in tempo reale
  - Wi-Fi tools per analisi delle reti wireless
  - Port scanner avanzato

- 🔐 **Modularità**
  - Ogni funzione è un modulo indipendente, facilmente aggiornabile
  - Interfaccia menu pulita, espandibile e semplice da usare

---

## 📂 Struttura del progetto

Ultimate-Hack-Suite/
│
├── main.py                     # Menu principale con interfaccia a tabella
├── requirements.txt            # Dipendenze Python
│
├── modules/
│   ├── bruteforce/             # Brute force tools
│   ├── exploits/               # Exploits in C e privilege escalation
│   ├── keylogger/              # Keylogger in Python
│   ├── network/                # Sniffer, scanner, Wi-Fi cracker
│   └── social_engineering/     # Phishing, simulazioni reali
│
└── assets/                     # HTML, payload, immagini, template

---

## 🧪 Fase di sviluppo

> 🚧 **Progetto attualmente in fase di test**

🧬 Ogni modulo viene testato singolarmente per garantire funzionalità reale e affidabile.  
📦 Il codice è funzionante ma potrebbe ricevere ulteriori aggiornamenti prima del rilascio pubblico.

❌ **Il download non è ancora disponibile al pubblico.**

---

## ⚙️ Requisiti

- Python 3.9+
- Compilatore GCC (per moduli C)
- PowerShell abilitato (per moduli remoti su Windows)
- Librerie Python (installabili con requirements.txt)

---

## 🔧 Installazione

Clona il repository e installa le dipendenze:

```bash
git clone https://github.com/R0b3r7R0gu3/Ultimate-Hack-Suite.git
cd Ultimate-Hack-Suite
pip install -r requirements.txt
python main.py

---
### 📲 Installazione su Termux

Assicurati di avere **Termux aggiornato**. Poi esegui questi comandi:

```bash
pkg update && pkg upgrade -y
pkg install git python clang -y
pip install --upgrade pip

# Clona il repository
git clone https://github.com/R0b3r7R0gu3/Ultimate-Hack-Suite.git
cd Ultimate-Hack-Suite

# Installa le dipendenze Python
pip install -r requirements.txt

# Rendi eseguibili gli script (solo se necessario)
chmod +x modules/scripts/*

# Avvia il tool
python main.py

---

### 🐉 Installazione su Kali Linux

Kali è il sistema operativo ideale per utilizzare **Ultimate-Hack-Suite**. Segui questi comandi per una configurazione rapida:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-pip gcc -y
pip3 install --upgrade pip

# Clona il repository
git clone https://github.com/R0b3r7R0gu3/Ultimate-Hack-Suite.git
cd Ultimate-Hack-Suite

# Installa le dipendenze Python
pip3 install -r requirements.txt

# Rendi eseguibili gli script C e PowerShell (se necessario)
chmod +x modules/scripts/*

# Avvia il tool
python3 main.py
