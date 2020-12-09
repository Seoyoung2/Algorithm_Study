# https://www.acmicpc.net/problem/12015
# N의 범위때문에 dp로 풀 수 없음 -> LIS(최장증가수열) 알고리즘 !

from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

res = [A[0]]
for i in range(1, N):
    if res[-1] < A[i]:
        res.append(A[i])
    else:
        res[bisect_left(res, A[i])] = A[i]
print(len(res))
