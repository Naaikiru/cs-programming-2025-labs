st = [('Мария', [3, 4, 4]), ('Кюнней', [3, 5, 5]), ('Андрей', [4, 5, 4]), ('Айсен', [5, 5, 4]), ('Дарина', [2, 2, 3])]
sl = {
    st[0][0]: round(sum(st[0][1])/3, 1),
    st[1][0]: round(sum(st[1][1])/3, 1),
    st[2][0]: round(sum(st[2][1])/3, 1),
    st[3][0]: round(sum(st[3][1])/3, 1),
    st[4][0]: round(sum(st[4][1])/3, 1)
}
st2 = []
st3 = []
for st1 in sl.items():
    st2.append(st1[1])
    st3.append(st1[0])
if max(st2):
    print(f'{st3[st2.index(max(st2))]} имеет наивысший средний балл: {max(st2)}')