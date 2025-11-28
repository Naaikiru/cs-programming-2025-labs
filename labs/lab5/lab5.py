# 1


a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
a = ', '.join(a)
if '3' in a:
    a = a.replace('3', '30', 1)
    print(a)


# 2

b = [2, 3, 4, 5, 6]
b = [b[0]**2, b[1]**2, b[2]**2, b[3]**2, b[4]**2]
print(b)


# 3

c = [2, 4, 5, 1, 34, 56]
print(max(c) // len(c))


# 4

def st(d):
    try:
        return tuple(sorted(d))
    except TypeError:
        return d
print(st((3, 1, 'rur', 5)))
print(st((45, 3, 2, 8, 0)))


# 5

e = {
    'apples': 200,
    'milk': 150,
    'noodle': 300,
    'chicken': 400,
    'beef': 600,
    'dumplings': 1100
}
emin = min(e, key=e.get)
eminp = e[emin]
emax = max(e, key=e.get)
emaxp = e[emax]
print(f'минимальная цена у {emin} - {eminp}')
print(f'максимальная цена у {emax} - {emaxp}')


# 6

f = ['apple', 200, 'kiwi', 450, 275, 'banana']
stri = []
inti = []
for i in (f):
    if type(i) == str:
        stri.append(i)
    if type(i) == int:
        inti.append(i)
f = {
    stri[0]: inti[0],
    stri[1]: inti[1],
    stri[2]: inti[2],
}
print(f)


# 7

j = {
    "привет": "hello",
    "пока": "bye",
    "игра": "game",
    "курица": "chiken",
    "диназавр": "dinosaur",
    "свитер": "sweater"
}
fd = False
jp = input('введите слово на русском: ')
for eng, rus in j.items():
    if jp == rus:
        print('перевод на английский: ', eng)
        fd = True
if not fd:
    print('слово не найденов словаре')


# 8

import random

igr1 = input('введите один из вариантов: камень, ножницы, бумага, ящерица, спок: ')
igr2 = ['ножницы', 'камень', 'бумага', 'спок', 'ящерица']
rnd = random.choice(igr2)
print(f'бот выбрал - {rnd}')

def f(x, y):
    if x == 'ножницы' and y == 'бумага': return ('вы победили!')
    elif x == 'бумага' and y == 'камень': return('вы победили!')
    elif x == 'камень' and y == 'бумага': return('вы победили!')
    elif x == 'ящерица' and y == 'бумага': return('вы победили!')
    elif x == 'спок' and y == 'бумага': return('вы победили!')
    elif x == 'ножницы' and y == 'бумага': return('вы победили!')
    elif x == 'ящерица' and y == 'бумага': return('вы победили!')
    elif x == 'бумага' and y == 'бумага': return('вы победили!')
    elif x == 'спок' and y == 'бумага': return('вы победили!')
    elif x == 'камень' and y == 'бумага': return('вы победили!')
    elif x == y: return ('ничья!')
    else: return('победитель бот!')

print(f(igr1, rnd))