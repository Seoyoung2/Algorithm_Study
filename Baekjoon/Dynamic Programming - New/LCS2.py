# https://www.acmicpc.net/problem/9252
# dp배열에 길이만 넣은 후, 다시 배열을 순회하며 문자열을 출력하였음
# --> 처음부터 dp배열에 문자열을 대입하는 방법 있음

from sys import stdin

A = " "+stdin.readline().rstrip()
B = " "+stdin.readline().rstrip()

dp = [[0] * len(B) for _ in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
res = dp[-1][-1]
print(res)

ans = []
for i in range(len(A)-1, 0, -1):
    for j in range(len(B)-1, 0, -1):
        if dp[i][j] == res and dp[i][j] != dp[i][j-1] and dp[i][j] != dp[i-1][j]:
            res -= 1
            ans.append(A[i])
            break
print("".join(reversed(ans)))
