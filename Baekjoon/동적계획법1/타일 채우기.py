# 3×N 크기의 벽을 2×1, 1×2 크기의 타일로 채우는 경우의 수를 구해보자.
# 입력 : 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 30)
# 출력 : 첫째 줄에 경우의 수를 출력한다.

# dp[n] = 3 * dp[n-2] + 2 * (dp[n-4] + dp[n-6] + ... + dp[0])
# n이 홀수면 타일로 채우기 불가능

import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(31)]
dp[0], dp[1], dp[2] = 1, 0, 3

for i in range(4, n+1, 2):
    dp[i] = 3 * dp[i-2]
    for j in range(4, i+1, 2):
        dp[i] += 2 * dp[i-j]
print(dp[n])