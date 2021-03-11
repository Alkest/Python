math = (input("Введите тип операции, которую хотите выполнить ('+','-','/','*','^','module','rand', 'fact','arccos'): "))
if math == "+" :
    x = (float(input("Введите значение x:\n")))
    y = (float(input("Введите значение y:\n")))
    print ("Результат: ", x+y)
elif math == "-" :
    x = (float(input("Введите значение x:\n")))
    y = (float(input("Введите значение y:\n")))
    print ("Результат: ", x-y)
elif math == "/" :
    x = (float(input("Введите значение x:\n")))
    y = (float(input("Введите значение y:\n")))
    if y :
        print ("Результат: ", x/y)
    else :
        print ("Деление на 0")
elif math == "*" :
    x = (float(input("Введите значение x:\n")))
    y = (float(input("Введите значение y:\n")))
    print ("Результат: ", x*y)
elif math == "^" :
    x = (float(input("Введите значение x:\n")))
    y = (float(input("Введите значение y:\n")))
    print ("Результат: ", x**y)
elif math == "module" :
    from math import fabs
    x = (float(input("Введите значение x:\n")))
    y = fabs(x)
    print ("Результат: ", y)
elif math == "rand" :
    import random
    x = random.randint(-100, 100)
    print ("Результат: ", x)
elif math == "fact" :
    import math
    x = int(input("Введите значение x:\n"))
    print("Результат: ", math.factorial(x))
elif math == "arccos" :
    import math
    x = float(input("Введите значение x:\n"))
    print("Результат: ", math.acos(x))