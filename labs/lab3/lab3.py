# 1

n = input('your name: ')
a = input('your age: ')
print((f'меня зовут {n} и мне {a} лет. ') * 10)


# 2

k = int(input('введите число от 1 до 9: '))
print('таблица умножения:')
print(f'{k} * 1 =', 1*k)
print(f'{k} * 2 =', 2*k)
print(f'{k} * 3 =', 3*k)
print(f'{k} * 4 =', 4*k)
print(f'{k} * 5 =', 5*k)
print(f'{k} * 6 =', 6*k)
print(f'{k} * 7 =', 7*k)
print(f'{k} * 8 =', 8*k)
print(f'{k} * 9 =', 9*k)
print(f'{k} * 10 =', 10*k)


# 3

for i in range(0, 100, 3):
    print(i)


# 4

n = int(input('введите число: '))
if n >= 0:
    f = n
    for i in range(2, n):
        f = f * i
    print(f)
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
    print(k, end= ' ')
    k, l = l, k + l


# 8

while True:
    n = input('Введите два числа через пробел: ')
    print(int(n[0]) + int(n[2]))