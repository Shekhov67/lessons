
#num_1 = input("Введите число: ")

#print("Ваше число: ", num_1)

#for i in "Hello World":
    #print(i)

#Списки
#n = int(input('Введи длину массива: '))
#user_list = []
#i = 0
#while i < n:
    #element = 'Добавьте элемент в массив #' + str(i + 1) + ': '
    #user_list.append(input(element))
    #i+=1

#print(user_list)

#Кортеж
#word = 'football, basketball, skate'
#hobby = word.split(', ')
#for i in range(len(hobby)):
#    hobby[i] = hobby[i].capitalize()
#result = ', '.join(hobby)
#print(result)

#Словари
# person = {
#     'user_1': {
#         'first_name': 'Andy',
#         'last_name': 'Shekh',
#         'age': 25,
#         'address': ('г.Москва', 'ул.Московская', 'д.27', 'кв.112'),
#         'parameters': {'rost': 175, 'weight': 75, 'penis': 16}
#     },
#     'user_2': {
#         "first_name": 'Margo',
#         "last_name": 'Smith',
#         "age": 23,
#         "address": ('г.Гагарин', 'ул.Театральная', 'д.29', 'кв.100'),
#         "parameters": {174, 55}
#     }
# }
#
# print(person["user_1"]["first_name"])
# print(person["user_1"]["last_name"])
# print(person["user_1"]["address"])
# print(person["user_1"]["parameters"]['penis'])

#Функции

# def minimal(l):
#     number = l[0]
#     for el in l:
#         if el < number:
#             number = el
#     print(number)
#
# numbers = [5, 2 ,5 , 8, 3, 56]
# minimal(numbers)

#Работа с файлами


# file = open("data/text.txt", 'a')
# file.write('Hello\n')
# file.write('!!!\n')
# file.close()

data = input("Введите текст:")
file = open('data/text.txt', 'a')
file.write(data + '\n')
file.close()
































