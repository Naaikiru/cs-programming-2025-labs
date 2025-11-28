# 2

a = int(input())
n = int(input())

def g(x, y):
    r = (x //10000)*0.3 
    pr = 0
    pr1 = []
    if n <= 3 : r += 3
    if 4 <= n <=6 : r += 5
    if n > 6 : r += 2
    for i in range(1, y+1):
        if (x+pr//10000) != r: 
            r = ((x+pr)//10000)*0.3
            pr = (x/100)*r
            pr1.append(pr)
    return pr1, sum(pr1)
print(g(a, n))