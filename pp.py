# r = int(input())

# print('1 матрица: ')
# r1 =[]
# for i in range(r):
#     h = input()
#     h = h.split(' ')
#     r1.append(h)
# for w in range(0, r):
#     if len(r1[w]) != r:
#         print('no')
#         print(quit())

# print('2 матрица: ')
# r2 =[]
# for i in range(r):
#     h = input()
#     h = h.split(' ')
#     r2.append(h)
# for w in range(0, r):
#     if len(r1[w]) != r:
#         print('no')
#         print(quit())
# d = []
# rr = int(r/2)
# for p in range(0, r):
#     for e in range(0, r):
#         d.append(int(r1[p][e]))
# d1 =[]
# for p in range(0, r):
#     for e in range(0, r):
#         d1.append(int(r2[p][e])) 

# n =[]
# n1 =[]
# for n2 in range(0, r):
#     for n3 in range(0, rr):
#         n.append(d[n3] + d1[n3])
#     for n3 in range(rr, r):
#         n1.append(d[n3] + d1[n3])

# for i in range(0, r):
#     print('сумма этих двух матриц: ')
#     print(str(n[i]), str(n1[i]))   
#     print(str(n[i]), str(n1[i]))
#     break

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