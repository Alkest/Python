number1 = int(input("Введите произвольное число: "))
number2 = int(input("Введите пограничное число: "))
if number1 < number2:
    print("1-ое число меньше пограничного")
if number1 > number2:
    print("1-ое число больше пограничного")
if number1 > number2*3:
    print("1-ое число больше пограничного более, чем в 3 раза")