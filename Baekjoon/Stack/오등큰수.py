# https://www.acmicpc.net/problem/17299
# A[i]의 오등큰수 : 오른쪽에 있으면서 수열 A에서 등장한 횟수가 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수
# 2중 for문으로 풀었더니 시간초과 ==> stack 사용했더니 통과

from sys import stdin

N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))    # [1, 1, 2, 3, 4, 2, 1]
# for문 안에서 count()함수 사용했더니 시간초과, O(n^2)인듯
# F = [L.count(L[i]) for i in range(N)]           # [3, 3, 2, 1, 1, 2, 3]
F = [0] * 1000001
for n in L:
    F[n] += 1                                   # [0, 3, 2, 1, 1]

# # stack 사용하지 않고 2중 for문으로 풀이 (시간초과)
# for i in range(N):
#     for j in range(i+1, N):
#         if F[j] > F[i]:
#             print(L[j], end=" ")
#             break
#     else:
#         print(-1, end=" ")

stack = []
ans = [-1 for _ in range(N)]
for i in range(N):
    while stack and F[L[stack[-1]]] < F[L[i]]:
        ans[stack.pop()] = L[i]
    stack.append(i)

print(*ans)                                      # -1, -1, 1, 2, 2, 1, -1
