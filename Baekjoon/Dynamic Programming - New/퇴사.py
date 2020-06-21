# https://www.acmicpc.net/problem/14501

# DP로 해결
from sys import stdin

n = int(stdin.readline())
dp = [0] * 20        # n일까지 번 돈
for day in range(n):
    t, p = map(int, stdin.readline().split())
    if dp[day+1] < dp[day]:
        dp[day+1] = dp[day]
    if dp[day] + p > dp[day+t]:
        dp[day+t] = dp[day] + p
print(dp[n])


# BFS로 해봤지만 실패.. 뭔가 놓친게 있는 듯 하다

# origin = list(tuple(map(int, stdin.readline().split())) for _ in range(n))
# answer = 0
# for idx in range(n):
#     day, sum = idx, 0
#     queue = deque(origin[idx:])
#     while queue:
#         time, pay = queue.popleft()
#         if day + time > n:
#             day += 1
#             continue
#         else:
#             day += time
#             sum += pay
#             for i in range(time-1):
#                 queue.popleft()
#     print(sum, day)
#     answer = max(answer, sum)
# print(answer)