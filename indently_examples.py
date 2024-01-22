#instead of using if and else conditional statements we can use dictionaries instead
# def first():
#     print("Calling: First")

# def second():
#     print("Calling: Second")

# def third():
#     print("Calling: Third")

# def default():
#     print("Calling: Default")

# var: int = int(input())

# # if var == 0:
# #     first()
# # elif var == 1:
# #     second()
# # elif var == 2:
# #     third()
# # else:
# #     default()

# funcs: dict = {0: first, 1: second, 2: third}

# final = funcs.get(var, default)

# final()
#----------------------------------------------------------------
# SETS

# set_a = {1,2,3}
# set_b = {2,3,4}

# print(set_a ^ set_b)  #prints the diference between two sets 
# print(set_a & set_b)  #prints the common elements in two sets

#----------------------------------------------------------------
# LISTS

# names = ['jayanth', ' shannu', 'sandy']
# print(max(names, key=len))

#----------------------------------------------------------------
# l = [i for i in range(5)]
# print(l)

# s = {i for i in range(5)}
# print(s)

# d = (('a',1),('b',2),('c',3),('d',4))
# k = {k: v for k, v in d}

# print(k)

# gen = (i for i in range(5))   # using generator function
# print(next(gen))   # prints 0
# print(next(gen))   # prints 1
# print(next(gen))   # prints 2
# print(next(gen))   # prints 3
# print(next(gen))   # prints 4

#----------------------------------------------------------------
# from random import choice #instead of importing randint

# l = ['a', 'b', 'c']

# # size = len(l)-1
# # r = randint(0,size)  # instead of using randint we use choice

# print(choice(l))
#----------------------------------------------------------------
# *_,='12345'
# print(_)  # prints  ['1', '2', '3', '4', '5']

# def send_mail(to: str) -> None:
#     print(f"Send email to :{to}")

# to = input()
# send_mail(to)

asteroids = [5, 10, -5]
if len(asteroids) < 2:
    print('The no of asteroids must be atleast 2')
elif len(asteroids) == 2:
    if abs(asteroids[0]) == abs(asteroids[1]):
        print([]);
    elif abs(asteroids[0]) > abs(asteroids[1]):
        print(asteroids[0])
    else:
        print(asteroids[1])
else:
    i = 0
    while i < len(asteroids)-1:
        if asteroids[i] > 0 and asteroids[i+1] < 0:
            if abs(asteroids[i]) == abs(asteroids[i+1]):
                asteroids.pop(i)
                asteroids.pop(i)
                i = 0
            elif abs(asteroids[i]) > abs(asteroids[i+1]):
                asteroids.pop(i+1)
                i = 0
            else:
                asteroids.pop(i)
                i = 0
        else:
            i += 1
    print(asteroids)