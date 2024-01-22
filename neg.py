import math
T = int(input())
for _ in range(T):
    X, Y, K = map(int, input().split())

    gcd_value = math.gcd(X, Y)
    lcm_value = (X * Y) // gcd_value

    if K % 2 == 0:
        print(2 * gcd_value)
    else:
        print(gcd_value + lcm_value)