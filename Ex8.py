# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Введите ширину шоколадкки: '))
height = int(input('Введите высоту шоколадкки: '))
slices = int(input('Введите количество кусочков: '))
if height == 1 and width * height > slices:
    print('Yes')
elif (slices % width == 0 or slices % height == 0) and width * height > slices:
    print('Yes')
else:
    print('No')