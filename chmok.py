vk = int(input('введите сумму, которую хотите вложить в банк: '))
sr = int(input('введите срок (в годах): '))

def obman(x, y):
    r1 = (x // 10_000)/10
    for r in range(1, y+1):
        if r1 >= 5:
            if sr <= 3:
                r1 += 3
                x += (x*r1/100)
            return x
print(obman(vk, sr))
