print("Вас приветствукт программа")
print( ">>Элементарный Калькулятор!<<")
print("Используйте  +  для сложения") 
print("Используйте  -  для вычитания")
print("Используйте  *  для умножения")
print("Используйте  /  для деления")

while True:
    Simb = input("введите знак >>>")
    if Simb in ('+', '-', '*', '/'):
        a = float(input("Первое число = "))
        b = float(input("Второе число = "))
        if Simb == '+':
            print(a + b)
        elif Simb == '-':
            print(a - b)
        elif Simb == '*':
            print(a * b)
        elif Simb == '/':
            if b != 0:
             print(a / b)
            else:
                print("!Деление на ноль, Вы считаете это возможным!?")
    else:
        print("Неверный знак операции!")