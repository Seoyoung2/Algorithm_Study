# 45656이란 수를 보자.
# 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)


# N[i] : 길이가 i인 계단 수의 총 개수 ( N[1]=9, N[2]=17 )
# N[i] = 2*N[i-1]-i
from sys import stdin

N = [9]
n = int(stdin.readline())
for i in range(1, n):
    N.append(2*N[i-1]-i)

print(N[-1])

# 간단한 점화식 찾았다고 생각하고 풀었지만 오답이었다.


# dp[i][j] : 길이가 i+1이고 j로 시작하는 수의 개수
dp = [[0 for _ in range(10)] for _ in range(n)]

for i in range(1, 10):
    dp[0][i] = 1
for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif j == 9:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n-1])%1000000000)

# DP로 해결한 코드