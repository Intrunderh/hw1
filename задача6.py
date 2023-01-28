chislo = (input('Введите шестизначный номер на билетике: '))
sleva = int(chislo[0]) + int(chislo[1]) + int(chislo[2])
sprava = int(chislo[3]) + int(chislo[4]) + int(chislo[5])
if sleva == sprava:
    print(f'Билетик под номером №{chislo} - является счастливым :D')
    print('Поздравляю Вас!!!')
else:
    print(f'Билетик под номером №{chislo} - не является счастливым!')