from itertools import batched
data: list[int] = [1,0,0,0,0,1,0,0]

batch: batched = batched(data,3)
print(list(batch))
