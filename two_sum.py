nums = list(map(int, input().split()))
target = int(input())
indices = {}
result = []

for i, num in enumerate(nums):
    if num in indices:
        result.extend([indices[num], i])
    else:
        indices[target - num] = i
print(result)
