def mkdict():
    list_one = input("Введите через запятую список слов: ").split(',')
    set_one = set(list_one)
    len_one = len(set_one)
    print('Количество слов в первом списке: ', len_one)
    list_two = input('Для формирования второго списка введите {} слов(а): '.format(len_one)).split(',')
    return dict(zip(set_one, list_two))


file_name = input('Введите имя файла: ')
file = open(file_name, 'w')
file.write(str(mkdict()))
file.close()
print('Словарь записан в файл {}'.format(file_name))
