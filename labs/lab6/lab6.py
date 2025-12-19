# 1

def f(x):
    if x[1] == 's' and x[2] == 'h': return float(x[0])/3600, 'h'
    elif x[1] == 'm' and x[2] == 'h': return float(x[0])/60, 'h'
    elif x[1] == 'h' and x[2] == 'm': return float(x[0])*60, 'm'
    elif x[1] == 'm' and x[2] == 's': return float(x[0])*60, 's'
    elif x[1] == 's' and x[2] == 'm': return float(x[0])/60, 'm'
    elif x[1] == 'h' and x[2] == 's': return float(x[0])*3600, 's'

x = input('введите время, ее измерение и измерение в которое хотите перевсти(через пробел): ')
x = x.split(' ')
x = str(f(x)[0]) + f(x)[1]
print(x)


# 3

def is_prime(n):
    if n <= 1:
         return False
    for i in range(2, int(n**0.5) + 1):
         if n % i == 0:
            return False
    return True

h = input('введите начало и конец диапозона: ')
h = h.split(' ')
k = []
h = [int(h[0]), int(h[1])]
for i in range(h[0], h[1]+1):
    if is_prime(i) == True:
        k.append(i)
if len(k) == 0:
    print('Error!')
else:
    print(k)


# 5

def poli():
    p = input('введите строку на проверку "является ли она полидромом": ').lower()
    p = p.replace(' ', '')

    if p == p[::-1]: return 'Да' 
    else: return 'Нет' 

print(poli())