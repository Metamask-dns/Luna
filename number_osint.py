from colorama import Fore

def phone_search(bd, bd1, bd2, bd3, bd4, bd5, bd6, bd7, phone1):
    Found = False
    with open(bd, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 2:
            phone = data[1]
            if phone1 in phone:
                id = data[0]
                username = data[2]
                last_name = data[3]
                first_name = data[4]
                print(Fore.BLUE + f'''
╔────────────────
│BaseData: Глаз Бога
│Номер телефона: {phone}
│ID: {id}
│Юзернейм: {username}
│Имя: {last_name}
│Фамилия:  {first_name} 
│Enter для возврата в меню
╚─────────────────
                      ''')
    with open(bd1, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                                      ''')
                Found = True

    with open(bd2, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                                      ''')
                Found = True

    with open(bd3, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                                      ''')
                Found = True

    with open(bd4, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                                      ''')
                Found = True

    with open(bd5, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                                      ''')
                Found = True

    with open(bd6, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 8:
                phone = data[7]
                if phone1 in phone:
                    user_id = data[0]
                    registration_date = data[1]
                    last_name = data[2]
                    first_name = data[3]
                    middle_name = data[4]
                    birthday = data[5]
                    gender = data[6]
                    email = data[8]
                    role = data[9]
                    class_name = data[13]
                    address = data[19]
                    country = data[16]
                    citizenship = data[15]
                    region = data[17]
                    municipal_education = data[18]
                    institution_name = data[20]
                    print(Fore.BLUE + f'''
╔────────────────                   
│База данных: PEREMENA (2024)
│Номер телефона: {phone}
│ID: {user_id}
│Зарегистрирован: {registration_date}
│Имя: {first_name}
│Фамилия: {last_name}
│Отчество: {middle_name}
│Почта: {email}
│Дата рождения: {birthday}
│Пол: {gender}
│Роль: {role}
│Буква класса: {class_name}
│Адрес: {address}
│Страна: {country}
│Населенный пункт: {citizenship}
│Регион: {region}
│Школа: {municipal_education}
│Порядковое имя: {institution_name}
│Enter для возврата в меню
╚─────────────────
                ''')
                Found = True

    with open(bd7, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 2:
            phone = data[0]
            if phone1 in phone:
                numbuster = data[2]
                getcontaco = data[3]
                print(Fore.BLUE + f'''
╔────────────────    
│База данных: GETCONTACT (2024)
│Номер телефона: {phone}
│{numbuster}
│{getcontaco}
│Enter для возврата в меню
╚─────────────────
                
                      ''')
                Found = True
            if not Found:
                print(Fore.BLUE + "Ничего не найдено по базам!")