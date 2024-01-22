import heapq

def sort_almost_sorted(arr, k):
    heap = arr[:k+1]
    heapq.heapify(heap)
    sorted_list = [] 

    for i in range(k+1, len(arr)):
        sorted_list.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        sorted_list.append(heapq.heappop(heap)) 

    return sorted_list
    
arr = list(map(int,input("Enter array Elements: ").split()))
k = int(input("K value: "))
print("Sorted array:", sort_almost_sorted(arr, k))
