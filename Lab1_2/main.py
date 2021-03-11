text = input("Введите произвольный текст: ")
counter = 1

for i in text:
    if counter == 3:
        counter += 1
        continue
    print(i, end ="")
    counter += 1

print("\n", len(text))
g = len(text)
counter = 1

for i in text:
    if counter == g:
        counter += 1
        continue
    print(i, end ="")
    counter += 1

if "с" in text:
    print("\nПрисутствует символ 'с'")

