l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

merged_l1 = int("".join(map(str, l1)))
merged_l2 = int("".join(map(str, l2)))

result = list(map(int, str(merged_l1 + merged_l2)))
result.reverse()
print(result)