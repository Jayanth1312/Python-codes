t = int(input())
while t>0:
    n,x,k = map(int,input().split()) # 8 8 3
    g = n-x
    
    boy_groups = x//k # 2
    girl_groups = g//k # 0
    
    r_boys = x%k  #2
    r_girls = g%k #0
    r_students = 0

    if g == 0:
        r_students = x
    if r_boys > 0:
        r_students += min(r_boys, girl_groups*k)
    if r_girls > 0:
        r_students += min(r_girls, boy_groups*k)
    
    print(r_students//k)
    t-=1