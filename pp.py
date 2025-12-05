r = int(input())

print('1 матрица: ')
r1 =[]
for i in range(r):
    k = []
    h = input()
    k.append(h.split(' '))
    r1.append(k)
    # if  ValueError:
    #     print('no')
    #     print(quit())
print(len(r1[0]))

# if len(r1[0]) != r:
#     print('no')
#     print(quit())

# print('2 матрица: ')
# r2 =[]
# for i in range(r):
#     k = []
#     h = input()
#     k.append(h.split(' '))
#     r2.append(k)
#     # if  ValueError:
#     #     print('no')
#     #     print(quit())
# if len(r2[0]) != r:
#     print('no')
#     print(quit())

# print(r1, r2)