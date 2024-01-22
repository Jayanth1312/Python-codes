def min_moves(T, test_cases):
    for _ in range(T):
        N, M, S, K = test_cases[_]
        min_moves = float('inf')
        for i in range(N - M + 1):
            max_moves = 0
            for j in range(M):
                diff = abs(int(S[i+j]) - int(K[j]))
                moves = min(diff, 10 - diff)
                max_moves = max(max_moves, moves)
            min_moves = min(min_moves, max_moves)
        print(min_moves)

T = int(input())
test_cases = []
for _ in range(T):
    N,M=map(int,input().split())
    S = input()
    K = input()
    test_cases.append((N, M, S, K))

min_moves(T, test_cases)