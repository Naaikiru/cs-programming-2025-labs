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
# h = [int(h[0]), int(h[1])]
for i in range(h[0], h[1]+1):
    if is_prime(i) == True:
        k.append(i)
if len(k) == 0:
    print('Error!')
else:
    print(k)