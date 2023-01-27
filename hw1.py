chislo = int(input('Введите трехзначное число: '))
summ = 0
while chislo > 0:
    summ += chislo % 10
    chislo /= 10
print(int(summ))