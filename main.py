
a = input("Введите первое слово:")
b = input("Введите второе слово:")
b = b[len(b)::-1]
if a == b:
    print("Слова являются анаграммами")
else:
    print("Слова не являются анаграммами")