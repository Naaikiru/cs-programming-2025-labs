r = int(input())

print('1 матрица: ')
r1 =[]
for i in range(r):
    h = input()
    h = h.split(' ')
    r1.append(h)
for w in range(0, r):
    if len(r1[w]) != r:
        print('no')
        print(quit())

print('2 матрица: ')
r2 =[]
for i in range(r):
    h = input()
    h = h.split(' ')
    r2.append(h)
for w in range(0, r):
    if len(r1[w]) != r:
        print('no')
        print(quit())
d = []
rr = int(r/2)
for p in range(0, r):
    for e in range(0, r):
        d.append(int(r1[p][e]))
d1 =[]
for p in range(0, r):
    for e in range(0, r):
        d1.append(int(r2[p][e])) 

n =[]
n1 =[]
for n2 in range(0, r):
    for n3 in range(0, rr):
        n.append(d[n3] + d1[n3])
    for n3 in range(rr, r):
        n1.append(d[n3] + d1[n3])

for i in range(0, r):
    print('сумма этих двух матриц: ')
    print(str(n[i]), str(n1[i]))   
    print(str(n[i]), str(n1[i]))
    break