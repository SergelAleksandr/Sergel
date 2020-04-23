print('Hello World! \n')

TEXT = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. "\
"А у нас управдом — друг человека!"
print(TEXT + "\n")

task1 = "1. Символов в тексте -  "
task01 = len(TEXT) 
print(task1 + str(task01) + "\n") 

task2 = "2. Инверсия текста - "
print(task2 + TEXT[::-1] + "\n")

task3 = "3. Все слова с заглавных - "
print(task3 + TEXT.title() + "\n")

task4 = "4. Весь текст прописными - "
print(task4 + TEXT.lower() + "\n")

task5 = "5. Число вхождений в строку \"нд\" = "
task51 = ". \"ам\" = "
task52 = ", \"о\" = "
nd = TEXT.count("нд")
am = TEXT.count("ам")
o = TEXT.count("о")
print(task5 + str(nd) + task51 + str(am) + task52 + str(o) + "\n")

task6 = "6. Все буквы заглавные - "
print(task6 + TEXT.upper())