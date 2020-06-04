# Heap (https://programmers.co.kr/learn/courses/30/lessons/42629)

# 이 풀이는 왜안되는지 모르겠음/;;
#def solution(stock, dates, supplies, k):
#     answer = 0
#     idx = 0
#     dates.append(k)
#     for i in range(k):
#         if i == dates[idx]:
#             # 남은 stock > 다음 공급일까지 먹을 밀가루 check
#             if stock < (dates[idx+1]-dates[idx]) or stock + sum(supplies[idx+1:]) < k - i:
#                 stock += supplies[idx]
#                 answer += 1
#             idx += 1
#         stock -= 1
#     return answer

import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    heap = []
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:
                idx = i + 1
                heapq.heappush(heap, -supplies[i])
            else:
                break
        stock -= heapq.heappop(heap)
        answer += 1
    return answer



print(solution(4, [4, 10, 15], [20, 5, 10], 30))        # 2
print(solution(4, [4], [20], 4))                        # 0
print(solution(4, [4, 8], [4, 4], 8))                   # 1
print(solution(4, [3, 8], [5, 4], 8))                   # 1
print(solution(10, [4, 5, 6], [300, 20, 30], 40))       # 1
print(solution(10, [1, 8, 10], [1, 1, 100], 100))       # 1

