students = [
    'Димова Александра Сергеевна',
    'Шапель Владимир Антононивч',
    'Зубакин Александр Сергеевич',
    'Митрохин Антон',
    'Синицына Лилия Дмитриевна',
    'Щегольков Никита Сергеевич',
    'Гребенщиков Богдан Вячеславович',
    'Ильина Мария Анатольевна',
    'Шубина Ольга Сергеевна',
    'Морозов Диман Физтеховец'
]

questons = []
for q in open('questons.txt', encoding="utf8").readlines():
    questons.append(q)

import random
print(random.choice(students) + str(':'), random.choice(questons) + "!")
