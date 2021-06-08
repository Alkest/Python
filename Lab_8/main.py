import math
import random

zero_args = {'rand'}
first_args = {'module', 'fact', 'arccos'}
second_args = {'+', '-', '/', '*', '^'}
class Calculator:
    def calc(self, operator, a=0.0, b=0.0):

        if operator in zero_args:
            return random.randint(-100, 100)

        elif operator in first_args:
            if operator == 'module':
                return abs(a)
            elif operator == 'fact':
                return math.factorial(a)
            elif operator == 'arccos':
                return math.acos(a)

        elif operator in second_args:
            if operator == '+':
                return a + b
            elif operator == '-':
                return a - b
            elif operator == '/':
                if b:
                    return a / b
                else:
                    print("Деление на 0")
                    return None
            elif operator == '*':
                return a * b
            elif operator == '^':
                return a ** b


operator = (input("Введите тип операции, которую хотите выполнить ('+','-','/','*','^','module','rand', 'fact','arccos'): "))
result = 0
mcalc = Calculator()

if operator in zero_args:
    result = mcalc.calc(operator)

elif operator in first_args:
    number_one = float(input("Введите число: "))
    result = mcalc.calc(operator, number_one)

elif operator in second_args:
    number_one = float(input("Введите первое число: "))
    number_two = float(input("Введите второе число: "))
    result = mcalc.calc(operator, number_one, number_two)

print("Результат: ", result)