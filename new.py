import random

t = int(input())

while t > 0:
    n = int(input())
    a = list(map(lambda x: int(input()), range(n)))
    b = list(map(lambda y: int(input()), range(n)))

    random.shuffle(a)
    random.shuffle(b)
    print(a)
    print(b)

    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    equal = all(element == c[0] for element in c)
    
    if equal:
        print(a)
        print(b)
    else:
        print('-1')
    t -= 1