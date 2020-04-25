print('\n')
print('Калькулятор индекса массы тела (ИМТ/BMI)' + '\n')

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

bmi = weight / (height * height)
print('Ваш ИМТ составляет: ', bmi)

ibmi = int(bmi)

if ibmi < 16:
    print('Выраженный дефицит массы тела')
else: 
    pass

if ibmi >= 16 and bmi < 18.5:
    print('Недостаточная масса тела')
else:
    pass

if ibmi >= 18.5 and bmi < 25:
    print('Нормальная масса тела')
else:
    pass

if ibmi >= 25 and bmi < 30:
    print('Избыточная масса тела (предожирение)')
else:
    pass

if ibmi >= 30 and bmi < 35:
    print('Ожирение 1-ой степени')
else:
    pass

if ibmi >= 35 and bmi < 40:
    print('Ожирение 2-ой степени')
else:
    pass

if ibmi >= 40:
    print('Ожирение 3-ой степени')
else:
    pass

if ibmi > 100:
    print('Проверьте введенные данные')
else:
    pass

print(str('0') + ('=' * int(ibmi - 1)) + '|' + ('=' * int(99 - ibmi)) + str('100'))
