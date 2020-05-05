while True:
    try:
        first = int(input('Введите первое число: '))
    except ValueError:
        print('Введите число')
    else:
        break

while True:
    try:
        second = int(input('Введите второе число: '))
    except ValueError:
        print('Введите число')
    else:
        break

while True:
    try:
        third = int(input('Введите третье число: '))
    except ValueError:
        print('Введите число')
    else:
        break

print('\n' + 'Первое задание: ')
print(not (first and second and third) or 'Нет нулевых значений!!!')

print('\n' + 'Второе задание: ')
print(first or second or third or 'Введены все нули!')

print('\n' + 'Третье задание: ')
if first > (second + third):
    print(first - second - third)
else:
    print("Условия не выполнены")

print('\n' + 'Четвертое задание: ')
if first < (second + third):
    print(second + third - first)
else:
    print("Условия не выполнены")

print('\n' + 'Пятое задание: ')
if (first > 50) and ((second or third) > first):
    print("Вася")
else:
    print("Условия не выполнены")

print('\n' + 'Шестое задание: ')
if (first > 5) or (second and third) == 7:
    print("Петя")
else:
    print("Условия не выполнены")