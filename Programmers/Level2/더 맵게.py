# Heap (https://programmers.co.kr/learn/courses/30/lessons/42626)


# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
#         answer += 1
#         scoville.append(scoville[0] + 2*scoville[1])
#         scoville = scoville[2:]
#         scoville.sort()
#     return answer

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2 * b)
    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))        # 2
print(solution([0, 0, 0, 1], 3))        # -1