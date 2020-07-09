# https://www.acmicpc.net/problem/1120

from sys import stdin

A, B = stdin.readline().split()
la, lb = len(A), len(B)

res = 0
for i in range(lb-la+1):
    tmp = 0
    for j in range(la):
        if A[j] == B[i+j]:
            tmp += 1
    res = max(res, tmp)
print(la - res)

# iai aiaia => 0
