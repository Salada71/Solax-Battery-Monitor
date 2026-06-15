#!/usr/bin/env python3
"""
Rychlý test - připojí se na Waveshare a vypíše surová RS-485 data.
Spuštění: python test_sniff.py
"""

import socket
import time

HOST = "192.168.85.198"
PORT = 502    # TCP port dle nastavení Waveshare
TIMEOUT = 10  # sekund čekání na první data

def hex_dump(data: bytes) -> str:
    hex_str = " ".join(f"{b:02X}" for b in data)
    ascii_str = "".join(chr(b) if 32 <= b < 127 else "." for b in data)
    return f"{hex_str:<48}  |{ascii_str}|"

print(f"Připojuji se na {HOST}:{PORT} ...")
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(TIMEOUT)
    sock.connect((HOST, PORT))
    print("Připojeno! Čekám na data ze sběrnice RS-485...\n")
except OSError as e:
    print(f"CHYBA připojení: {e}")
    print(f"\nTipy:")
    print(f"  - Zkontroluj IP adresu a port v nastavení Waveshare")
    print(f"  - V web UI Waveshare musí být nastaven 'Transparent mode'")
    input("\nStiskni Enter pro ukončení...")
    exit(1)

total = 0
buf = bytearray()
start = time.monotonic()

try:
    while True:
        try:
            chunk = sock.recv(256)
            if not chunk:
                print("Spojení ukončeno serverem.")
                break
            buf.extend(chunk)
            total += len(chunk)
            # Tiskni po řádcích po 16 bajtech
            while len(buf) >= 16:
                line = bytes(buf[:16])
                del buf[:16]
                print(hex_dump(line))
        except socket.timeout:
            if total == 0:
                elapsed = time.monotonic() - start
                print(f"Za {elapsed:.0f}s nepřišla žádná data.")
                print("Zkontroluj:")
                print("  - Je střídač zapnutý a komunikuje s bateriemi?")
                print("  - Je Waveshare v Transparent mode?")
                print("  - Správné zapojení RJ-45 na poslední slave baterii?")
            else:
                # Vytiskni zbytek bufferu
                if buf:
                    print(hex_dump(bytes(buf)))
                    buf.clear()
                print(f"\n-- pauza (celkem přijato {total} bajtů) --\n")
            sock.settimeout(TIMEOUT)

except KeyboardInterrupt:
    print(f"\n\nUkončeno. Celkem přijato: {total} bajtů.")
finally:
    sock.close()

input("\nStiskni Enter pro ukončení...")
