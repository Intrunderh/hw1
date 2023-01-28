# Найдите сумму цифр трехзначного числа
chislo = int(input('Введите трехзначное число: '))
summ = 0
while chislo > 0:
    summ += chislo % 10
    chislo //= 10
print((f'Сумма цифр трехзначного числа = {summ}'))