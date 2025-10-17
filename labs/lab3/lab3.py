# 1

n = input('your name: ')
a = input('your age: ')
print((f'меня зовут {n} и мне {a} лет. ') * 10)


# 2

k = int(input('введите число от 1 до 9: '))
print(f'таблица умножения числа {k}:')

n = 1
while n <= 10:
    print(f'1 * {n} = ', k*n)
    n += 1


# 3

for i in range(0, 100, 3):
    print(i)


# 4

n = int(input('введите число: '))
if n >= 0:
    f = n
    for i in range(2, n):
        f = f * i
    print(f'факториал числа {n}: ',f)
else:
    print('нет, введите другое')


# 5

n = 20
while n >= 0:
    print(n)
    n = n - 1


# 6

n = int(input('введите число: '))
k = 0
l = 1
while k <= n:
    print(k, end= '; ')
    k, l = l, k + l


# 8

while True:
    n = input('Введите два числа через пробел: ')
    f = n.split(' ')
    print(int(f[0]) + int(f[1]))


