# https://www.acmicpc.net/problem/2352
# Greedy 카테고리지만 dp가 생각나서 dp로 품

from sys import stdin

n = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

ans = [1] * n
for i in range(n):
    for j in range(i):
        if L[i] > L[j]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans))