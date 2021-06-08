list_one = input("Введите через запятую список слов: ").split(',')
set_one = set(list_one)
len_one = len(set_one)
print('Количество слов в первом списке: ', len_one)
list_two = input('Для формирования второго списка введите {} слов(а): '.format(len_one)).split(',')
Dict = dict(zip(set_one, list_two))
print(Dict)

