n = int(input('Введите n долек: '))
m = int(input('Введите m долек: '))
k = int(input('Введите k долек: '))
# if (m * n) % k:
if k < m * n and (k % m == 0 or k % n == 0):
    print('Yes')
else:
    print('No')
