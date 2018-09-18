students = [
    'Димова Александра Сергеевна',
    'Зубакин Александр Сергеевич',
    'Митрохин Антон',
    'Синицына Лилия Дмитриевна',
    'Шапель Владимир Антонович',
    'Щегольков Никита Сергеевич',
    'Гребенщиков Богдан Вячеславович',
    'Ильина Мария Анатольевна',
    'Шубина Ольга Сергеевна',
]

questons = []
for q in open('questons.txt').readlines():
    questons.append(q)

import random
print(random.choice(students) + str(':'), random.choice(questons))
