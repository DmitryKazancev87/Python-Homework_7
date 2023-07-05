# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять
# из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу
# с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке
# и “Пам парам”, если с ритмом все не в порядке.

def pux (str):
    str=str.split()
    list=[]
    for word in str:
        result=0
        for vowel in word:
            if vowel in 'аеёиоуыэюя':
                result+=1
        list.append(result)
    return len(list)==list.count(list[0])
str= input("Введите стихотворение :")
if pux(str):
    print("Парам пам-пам")
else:
    print("Пам парам")    


# Вариант исполнения №2:
# def count_vowels(word):
#     vowels = 'аеёиоуыэюя'

#     count=0
#     for letter in word:
#         if letter.lower in vowels:
#             count += 1
#     return count

# def check_rhythm(poem):
#     phrases = poem.split()
#     for phrase in phrases:
#         words = phrase.split('-')
#         vowel_counts = [count_vowels(word) for word in words]
#         if len(set(vowel_counts)) > 1:
#             return "Пам парам"
#     return "Парам пам-пам"

# poem = input("Введите стихотворение: ")
# result = check_rhythm(poem)
# print(result)