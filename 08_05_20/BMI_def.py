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
        input_user()
    elif answer == 2:
        # search_user()
        # calc = search_user()
        calc_user()
    elif answer == 3:
        # search_for_del()
        # away = search_for_del()
        del_user()
    
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
        sex = str(input('Выберите пол (М/Ж): '))
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
    global bmi_list
    values = [weight, height, sex, age]
    if bmi_list == None:
        bmi_list = {name : values}
    else:
        bmi_list[name] = values
    # bmi_list = {name : {'Рост' : height, 'Пол' : sex, 'Возраст' : age}}
    # new = {'ФИО' : name, 'Рост' : height, 'Пол' : sex, 'Возраст' : age}
    # global bmi_list
    # key = str(uuid.uuid4())
    # bmi_list[str(uuid.uuid4())] = new


# def save_user(new_user):
#     global bmi_list
#     key = str(uuid.uuid4())
#     bmi_list[str(uuid.uuid4())] = {new_user}
#     print(bmi_list)
    



# def search_user():
    # for values in bmi_list.items:
    #     print(value)
    # calc = input('Введите пользователя: ')
    # print(calc)
    # get_calc = bmi_list.get[calc]
    # for value in get_calc:
    #     print(calc)
    # else:
    #     print('Нет такого пользователя, повторите попытку: ')
    # return calc
    
def calc_user(): 
    print(list(bmi_list))
    calc = input('Напишите ФИО пользователя из списка: ')
    print(bmi_list[calc])
        
    bmi = bmi_list[calc][0] / (bmi_list[calc][1] ** 2)
    
    # bmi_calc = bmi_list.get[calc, None]   
    # bmi = bmi_calc[1] / (bmi_calc[2] ** 2)
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

# def search_for_del():
#     for _, value in bmi_list.items:
#         print(value)
#     away = input('Введите пользователя из спискадля удаления: ')
#     for away in bmi_list.items:
#         print(away)
#     return away

def del_user():
    global bmi_list
    print(list(bmi_list))
    away = input('Напишите ФИО пользователя из списка: ')
    while True:
        ans = str(input('Вы действительно хотите удалить данного пользователя? (yes или no) '))
        if ans == 'yes':
            bmi_list.pop(away) 
            break
        else:
            print('Повторите выбор (yes/no)') 
    return bmi_list


def main():
    while True:
        main_menu()
        answer = choise()
        if answer == 4:
            break
        choise_options(answer)
        


if __name__ == "__main__":
    main()