import uuid
num = 1
bmi_list = {}

name = 'ФИО'
weight = 'Вес'
height = 'Рост'
sex = 'Пол'
age = 'Возраст'

def main_menu():
    print('\n' + 'Выберите команду: \n'
        '1. Новый пользователь \n'
        '2. Расчет \n'
        '3. Удаление пользователя \n'
        '4. Выход \n'
        '(Выберите "1", "2", "3" или "4")')
    pass

def choise():
    while True:
        try:
            choice = int(input())
        except ValueError:
            print('Введите число')
        else:
            break
    return int(choice)
            
def choise_options(answer):
    if answer == 1:
        new = input_user()
        save_user(new)
    elif answer == 2:
        calc = search_user()
        calc_user(calc)
    elif answer == 3:
        away = search_for_del()
        del_user(away)
    
    # elif answer != (1 or 2 or 3):
    #     print('Введите число от 1 до 4')

def input_user():
    name = str(input('Введите ФИО: '))
    while True:
        try:
            weight = float(input('Введите вес (кг.): '))
        except ValueError:
            print('Введите число')
        else:
            break
    while True:
        try:
            height = float(input('Введите рост (м.): '))
        except ValueError:
            print('Введите число')
        else:
            break
    while True:
        sex = str(input('Выберите пол (М/Ж): ').upper())
        if sex == 'М':
            True
            break
        elif sex == 'Ж':
            True
            break
        else:
            print('Повторите выбор (М/Ж)')
    while True:
        try:
            age = float(input('Введите возраст: '))
        except ValueError:
            print('Введите число')
        else:
            break
    new = {'ФИО' : name, 'Вес' : weight, 'Рост' : height, 'Пол' : sex, 'Возраст' : age}
    return new

def save_user(new):
    global bmi_list
    bmi_list[str(uuid.uuid4())] = new
    print(bmi_list.values())
  
def search_user():
    print(list(bmi_list.values()))
    calc = input('Введите пользователя: ')
    for calc in bmi_list:
        break
    else:
        print('Нет такого пользователя. Повторите попытку: ')
    return calc
    
def calc_user(calc): 
    cool = bmi_list[calc]
    print(cool)
    bmi = cool['Вес'] / (cool['Рост'] ** 2)
    
    print('Ваш ИМТ составляет: ', bmi)
    ibmi = int(bmi)
    if ibmi > 100:
        print('Проверьте введенные данные')
    elif ibmi < 16:
        print('Выраженный дефицит массы тела')
    elif ibmi >= 16 and ibmi < 18.5:
        print('Недостаточная масса тела')
    elif ibmi >= 18.5 and ibmi < 25:
        print('Нормальная масса тела')
    elif ibmi >= 25 and ibmi < 30:
        print('Избыточная масса тела (предожирение)')
    elif ibmi >= 30 and ibmi < 35:
        print('Ожирение 1-ой степени')
    elif ibmi >= 35 and ibmi < 40:
        print('Ожирение 2-ой степени')
    elif ibmi >= 40 and ibmi <100:
        print('Ожирение 3-ой степени')
    else:
        pass
    if ibmi <100:
        print(str('0') + ('=' * int(ibmi - 1)) + '|' + ('=' * int(99 - ibmi)) + str('100'))

def search_for_del():
    print(list(bmi_list.values()))
    user_del = input('Введите пользователя для удаления: ')
    for user_del in bmi_list:
        break
    else:
        print('Нет такого пользователя. Повторите попытку: ')
    return user_del

def del_user(away):
    global bmi_list
    out_away = bmi_list[away]
    print(out_away)
    def get_key(bmi_list, out_away):
        for k, v in bmi_list.items():
            if v == out_away:
                return k
    while True:
        ans = str(input('Вы действительно хотите удалить данного пользователя? (yes или no) '))
        if ans == 'yes':
            bmi_list.pop(get_key(bmi_list, out_away)) 
            break
        else:
            print('Повторите выбор (yes/no)') 
    return bmi_list.values()


def main():
    print('Калькулятор индекса массы тела')
    while True:
        main_menu()
        answer = choise()
        if answer == 4:
            break
        choise_options(answer)
        


if __name__ == "__main__":
    main()