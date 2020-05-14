def gener():
    num = 1
    while num < 100:
        yield num
        num += 1
for n in gener():
    if n % 3 == 0:
        print('Василий')
    else:
        print(n)