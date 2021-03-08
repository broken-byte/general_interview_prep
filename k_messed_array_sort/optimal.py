from heapq import heappop, heappush, heapify


def optimal(arr, k):  # O(n*log(k))
    n = len(arr)
    min_heap = arr[:k + 1]
    heapify(min_heap)
    target_index = 0
    for remaining_index in range(k + 1, n):
        arr[target_index] = heappop(min_heap)
        heappush(min_heap, arr[remaining_index])
        target_index += 1
    while min_heap:
        arr[target_index] = heappop(min_heap)
        target_index += 1
    return arr
