# 1

t = int(input('введите температуру: '))
if t >= 20:
    print('кондиционер включен')
else:
    print('кодниционер выключен')


# 2

m = int(input('введите нмоер месяца: '))
if m <= 2 or m == 12:
    print('это зима')
elif 3 <= m <= 5:
    print('это весна')
elif 6 <= m <= 8:
    print('это лето')
else:
    print('это осень')


# 3

try:
    da = input('введите возраст собаки(в годах): ')
    g = 10.5
    if int(da) < 1:
        print('возраст должен быть не меньше 1 года')
    elif int(da) == 1:
        da = g
        print('возраст собаки в человеческих годах: ', da)
    elif int(da) == 2:
        da = g*2
        print('возраст собаки в человеческих годах: ', da)
    elif 2 < int(da) <= 22:
        da = g*2 + (int(da) - 2)*4
        print('возраст собаки в человеческих годах: ', da)
    elif int(da) > 22:
        print('возраст должен быть не больше 22')
except ValueError:
    print("Ошибка: введите число")


# 4

r = int(input('введите число: '))
if r % 2 == 0 and r % 3 == 0:
    print('число делиться на 6')
else:
    print('число не делиться на 6')


# 6

y = int(input('введите год: '))
if y % 4 == 0:
    if y % 100 != 0 or y % 400 == 0:
        print("Високосный год")
    else:
        print("Не високосный год")
else:
    print("Не високосный год")


# 7

ch = input('введите три числа чрез пробел: ')
f = ch.split(' ')
print(min(int(f[0]), int(f[1]), int(f[2])))


# 8

su = int(input('введите сумму покупок: '))
if su < 1000:
    print('скидка 0% ')
    print('к оплате: ', su)
elif 1000 <= su < 5000:
    print('скидка 5% ')
    print('к оплате: ', su - (su*0.05))
elif 5000 <= su < 10000:
    print('скидка 10% ')
    print('к оплате: ', su - (su*0.1))
elif 10000 <= su:
    print('скидка 15% ')
    print('к оплате: ', su - (su*0.15))


# 9

m = int(input('введите час (0-23): '))
if  6 <= m <= 11:
    print('сейчас утро')
elif 12 <= m <= 17:
    print('сейчас день')
elif 18 <= m <= 23:
    print('сейчас вечер')
else:
    print('сейчас ночь')


# 10

h = int(input('введите число: '))
def is_prime(n):
    if n <= 1:
         return False
    for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
            return False
    return True
if is_prime(h) == True:
    print(f'{h} - простое число')
else:
    print(f'{h} - состовное число')
    