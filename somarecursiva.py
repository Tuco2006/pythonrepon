def soma(l):
    if len(l) == 1:
        return l[0]
    return l[0] + soma(l[1:])

l = [1, 2, 3, 4, 5, 6, 7]

print(soma(l))
