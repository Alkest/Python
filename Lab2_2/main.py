a = input("Введите название первого овоща: ")
b = input("Введите название второго овоща: ")
c = input("Введите название третьего овоща: ")
print (a.lower(),b.lower(),c.lower())
print (a.upper(),b.upper(),c.upper())
print(a.capitalize(),b.capitalize(),c.capitalize())
print("Введите количество для ", a, " ")
countA = int(input())
print("Введите количество для ", b, " ")
countB = int(input())
print("Введите количество для ", c, " ")
countC = int(input())
print ("   Овощ             Количество   ")
print("{0:^11} {1:^27}" .format(a,countA))
print("{0:^11} {1:^27}" .format(b,countB))
print("{0:^11} {1:^27}" .format(c,countC))