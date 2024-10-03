from colorama import Fore
def telegram_search(id_bd, id_input):
    Found = False
    with open(id_bd, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 2:
            id_stol = data[4]
            if id_input in id_stol:
                system_number = data[0]
                name = data[1]
                last_name = data[2]
                phone_number = data[3]
                nick_name = data[5]
                was_online = data[6]
                print(Fore.BLUE + f'''
╔────────────────
│BaseData: Telegram
│Номер телефона: {phone_number}
│ID: {id_stol}
│Юзернейм: {nick_name}
│Имя: {name}
│Фамилия:  {last_name} 
│Системный номер: {system_number}
│Был в сети: {was_online}
│Enter для возврата в меню
╚─────────────────
                      ''')
                Found = True
            if not Found:
                print(Fore.BLUE + "В базе ничего не найдено!")

def username(id_bd, username_input):
    Found = False
    with open(id_bd, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split('|')
        if len(data) >= 2:
            nick_name = data[5]
            if username_input in nick_name:
                system_number = data[0]
                name = data[1]
                last_name = data[2]
                phone_number = data[3]
                id_stol = data[4]
                nick_name = data[5]
                was_online = data[6]
                print(Fore.BLUE + f'''
    ╔────────────────
    │BaseData: Telegram
    │Номер телефона: {phone_number}
    │ID: {id_stol}
    │Юзернейм: {nick_name}
    │Имя: {name}
    │Фамилия:  {last_name} 
    │Системный номер: {system_number}
    │Был в сети: {was_online}
    │Enter для возврата в меню
    ╚─────────────────
                          ''')
                Found = True
            if not Found:
                print(Fore.BLUE + "В базе ничего не найдено!")