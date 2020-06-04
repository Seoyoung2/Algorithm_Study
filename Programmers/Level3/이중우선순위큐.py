# Heap (https://programmers.co.kr/learn/courses/30/lessons/42628)

import heapq

def solution(operations):
    heap = []
    for op in operations:
        if op[0] == "I":
            heapq.heappush(heap, int(op[2:]))
        elif heap:
            if int(op[2:]) == 1:
                heap.sort()
                heap.pop()
            else:
                heapq.heappop(heap)
    return [max(heap), heap[0]] if len(heap) else [0, 0]


print(solution(["I 16", "D 1"]))        #[0, 0]
print(solution(["I 7", "I 5", "I -5", "D -1"]))        #[7, 5]
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"])) #[6, 5]