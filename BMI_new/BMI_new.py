print('\n' + 'Калькулятор индекса массы тела (ИМТ/BMI)' + '\n')

dlist = {}
name = 'ФИО'
weight = 'Вес'
height = 'Рост'
sex = 'Пол'
age = 'Возраст'

while True:
    values = [weight, height, sex, age]
    if dlist == None:
        dlist = {name : values}
    else:
        dlist[name] = values
   
    print('\n' + 'Выберите команду: \n'
        '1. Новый пользователь \n'
        '2. Расчет \n'
        '3. Данные \n'
        '(Выберите "1", "2" или "3")')
    
    while True:
        try:
            choice = int(input())
        except ValueError:
            print('Введите число')
        else:
            break

    if choice == 1:
        name = str(input('Введите Ваше ФИО: '))
        while True:
            try:
                weight = float(input('Ваш вес (кг.): '))
            except ValueError:
                print('Введите число')
            else:
                break
        while True:
            try:
                height = float(input('Ваш рост (м.): '))
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
                age = float(input('Ваш возраст: '))
            except ValueError:
                print('Введите число')
            else:
                break
    
    if choice == 2:
        print(list(dlist))
        user = input('Напишите ФИО пользователя из списка: ')
        print(dlist[user])
        weight = dlist[user][0]
        height = dlist[user][1]
    
        bmi = weight / (height ** 2)
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
        else:
            break
    
    if choice == 3:
        print(dlist)
        exit
    