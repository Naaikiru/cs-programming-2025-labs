

def sort_tuple(t):
    try:
        return tuple(sorted(t))
    except TypeError:
        return t
print(sort_tuple((3, 1, 'rur', 5)))
print(sort_tuple((45, 3, 2, 8, 0)))
