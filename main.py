lst=list(range(1000))

#Обратный перебор
def answer1(spisok):
    rew=[] #Создать список
    for i in range(spisok[len(spisok)-1], -1, -1): #Перебор от 999 до 0
        rew.append(spisok[i])
    return rew
print(answer1(lst))
#Недостаток: функция ломается, если lst содержит иные исходные данные, например range(5, 1000, 20)

#Вычитание из длины списка
def answer2(spisok):
    rew=[] #Создать список
    for i in spisok:
        rew.append(spisok[len(spisok)-1]-i) # Добавить к списку значение = длина списка - i (999-0, 999-1, 999-2, ... 999-999)
    return rew
print(answer2(lst))
#Недостаток: Так как функция создавалась с расчетом на то, что lst[0]=0, то функция работает некорректно,
# если если lst содержит иные исходные данные, например range(5, 1000, 20)

#Через словарь
def answer3(spisok):
    rew={}
    for i in range(len(spisok)):
        rew[i]=spisok[len(spisok)-1]-spisok[i] #Ключ : Список с индексом [длина списка - ключ] (0:999, 1:998, ..., 999:0)

    return list(rew.values())# Возвращаем список со значениями
print(answer3(lst))
#Недостаток: Так как функция создавалась с расчетом на то, что lst[0]=0, то функция работает некорректно,
# если если lst содержит иные исходные данные, например range(5, 1000, 20), так как вычитается не 0, а 5

# Добавляем в начало
def answer4(spisok):
    rew=[]
    for i in spisok:
       rew.insert(0, i) # Перебираем список и добавляем значение в начало нового списка (индекс = 0)
    return rew
print(answer4(lst))
#Недостаток: некрасивое решение, так как использован другой метод списка

def answer5(spisok): return spisok[::-1]
print(answer5(lst))
#Недостаток: слишком мало




