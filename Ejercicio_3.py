def power(x, y):
    ''' Funcion para culcular la exponenciacion x**y
    '''
    if y == 1:
        return x

    else:
        return x * power(x, y - 1)


def power_v2(x, y):
    '''Funcion para culcular la exponenciacion x**y
    version alternativa
    '''
    if y == 0:
        return 1
    elif y % 2 == 0:
        return power_v2(x * x, y / 2)
    else:
        return x * power_v2(x * x, (y - 1) / 2)

x = 2
y = 4

print(power(x, y))
print(power_v2(x, y))