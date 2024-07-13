m = 4
n = 7

for i in range(m):
    str = ''
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                str += '/¯\\' if i == 0 else '/ \\'
            else:
                str += '_'
        else:
            if j % 2 == 0:
                str += '\\_/'
            else:
                str += ' '
    print(str)
