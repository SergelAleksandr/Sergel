import datetime
import time
import os

symbol = '\u2593'
def line1():
    return (symbol * 8)
def line2():
    return (symbol * 2 + '    ' + symbol * 2)
def line3():
    return ('  ' + symbol * 4 + '    ')
def line4():
    return ('    ' + symbol * 2 + '    ')
def line5():
    return ('  ' + symbol * 6 + '  ')
def line6():
    return ('      ' + symbol * 2)
def line7():
    return (symbol * 2 + '      ')
def line8():
    return ('    ' + symbol * 4)
def line9():
    return ('    ')
def line10():
    return (' ' + symbol * 2 + ' ')

def replace1():
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for element in str_now:
        if element == '1':
            element = line3()
            asd.append(element)
        elif element == '2':
            element = line1()
            asd.append(element)
        elif element == '3':
            element = line1()
            asd.append(element)
        elif element == '4':
            element = line2()
            asd.append(element)
        elif element == '5':
            element = line1()
            asd.append(element)
        elif element == '6':
            element = line1()
            asd.append(element)
        elif element == '7':
            element = line1()
            asd.append(element)
        elif element == '8':
            element = line1()
            asd.append(element)
        elif element == '9':
            element = line1()
            asd.append(element)
        elif element == '0':
            element = line1()
            asd.append(element)
        elif element == '.':
            element = line9()
            asd.append(element)
    myString = ' '.join(asd)
    print(myString)
def replace2():
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for element in str_now:
        if element == '1':
            element = line4()
            asd.append(element)
        elif element == '2':
            element = line6()
            asd.append(element)
        elif element == '3':
            element = line6()
            asd.append(element)
        elif element == '4':
            element = line2()
            asd.append(element)
        elif element == '5':
            element = line7()
            asd.append(element)
        elif element == '6':
            element = line7()
            asd.append(element)
        elif element == '7':
            element = line6()
            asd.append(element)
        elif element == '8':
            element = line2()
            asd.append(element)
        elif element == '9':
            element = line2()
            asd.append(element)
        elif element == '0':
            element = line2()
            asd.append(element)
        elif element == '.':
            element = line9()
            asd.append(element)
    myString = ' '.join(asd)
    print(myString)
def replace3():
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for element in str_now:
        if element == '1':
            element = line4()
            asd.append(element)
        elif element == '2':
            element = line1()
            asd.append(element)
        elif element == '3':
            element = line8()
            asd.append(element)
        elif element == '4':
            element = line1()
            asd.append(element)
        elif element == '5':
            element = line1()
            asd.append(element)
        elif element == '6':
            element = line1()
            asd.append(element)
        elif element == '7':
            element = line6()
            asd.append(element)
        elif element == '8':
            element = line1()
            asd.append(element)
        elif element == '9':
            element = line1()
            asd.append(element)
        elif element == '0':
            element = line2()
            asd.append(element)
        elif element == '.':
            element = line9()
            asd.append(element)
    myString = ' '.join(asd)
    print(myString)
def replace4():
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for element in str_now:
        if element == '1':
            element = line4()
            asd.append(element)
        elif element == '2':
            element = line7()
            asd.append(element)
        elif element == '3':
            element = line6()
            asd.append(element)
        elif element == '4':
            element = line6()
            asd.append(element)
        elif element == '5':
            element = line6()
            asd.append(element)
        elif element == '6':
            element = line2()
            asd.append(element)
        elif element == '7':
            element = line6()
            asd.append(element)
        elif element == '8':
            element = line2()
            asd.append(element)
        elif element == '9':
            element = line6()
            asd.append(element)
        elif element == '0':
            element = line2()
            asd.append(element)
        elif element == '.':
            element = line9()
            asd.append(element)
    myString = ' '.join(asd)
    print(myString)
def replace5():
    now = datetime.datetime.now().time()
    str_now = list(now.strftime('%H.%M.%S'))
    asd = []
    for element in str_now:
        if element == '1':
            element = line5()
            asd.append(element)
        elif element == '2':
            element = line1()
            asd.append(element)
        elif element == '3':
            element = line1()
            asd.append(element)
        elif element == '4':
            element = line6()
            asd.append(element)
        elif element == '5':
            element = line1()
            asd.append(element)
        elif element == '6':
            element = line1()
            asd.append(element)
        elif element == '7':
            element = line6()
            asd.append(element)
        elif element == '8':
            element = line1()
            asd.append(element)
        elif element == '9':
            element = line1()
            asd.append(element)
        elif element == '0':
            element = line1()
            asd.append(element)
        elif element == '.':
            element = line10()
            asd.append(element)
    myString = ' '.join(asd)
    print(myString)

def clear():
    os.system('cls')

def main():
    while True:
        replace1()
        replace2()
        replace3()
        replace4()
        replace5()
        time.sleep(1)
        clear()

if __name__ == "__main__":
    main()