print("Введите два числа через пробел")
a, b = map(int, input().split())
print("Сумма чисел:", a+b)
print("Разность чисел:", a-b)
print("Среднее арифметическое модулей чисел:", (abs(a)+abs(b))/2)
