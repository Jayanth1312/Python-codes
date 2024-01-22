def min_balloons_to_take_out(R, G, B, K):
    balloons = [R, G, B]
    balloons.sort()
    if balloons[0] >= K:
        return 3 * (K - 1) + 1
    elif balloons[1] >= K:
        return balloons[0] + 2 * (K - 1) + 1
    else:
        return balloons[0] + balloons[1] + K


# Read the number of test cases
T = int(input())
for _ in range(T):
    R, G, B = map(int, input().split())
    K = int(input())
    result = min_balloons_to_take_out(R, G, B, K)
    print(result)
