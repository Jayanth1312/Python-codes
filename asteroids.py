l = list(map(int, input().split()))
# [5, 10, -5]
if len(l) < 2:
    i = 0
    while i < len(l)-1:
        if l[i] > 0 and l[i+1] < 0:
            if abs(l[i]) == abs(l[i+1]):
                l.pop(i)
                l.pop(i)
                i=0
            elif abs(l[i]) > abs(l[i+1]):
                l.pop(i+1)
                i=0
            else:
                l.pop(i)
                i=0
        else:
            i+=1
    print(l)