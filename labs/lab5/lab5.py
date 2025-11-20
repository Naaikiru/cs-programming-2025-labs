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

