def fat(l):
    if l == 1:
        return l
    return l * fat(l - 1)

print(fat(7))