# Задание 4.
# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
spisok = input("Введите целые числа через пробел: ").split( )
el = 0
for elem in range(int(len(spisok)/2)) :
    spisok[el] , spisok [el + 1] = spisok [el + 1] , spisok[el]
    el += 2
print (spisok)
