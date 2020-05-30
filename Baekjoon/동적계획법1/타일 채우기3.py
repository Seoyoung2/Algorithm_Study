# 2×N 크기의 벽을 2×1, 1×2, 1×1 크기의 타일로 채우는 경우의 수를 구해보자.
# 입력 : 첫째 줄에 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 출력 : 첫째 줄에 경우의 수를 1,000,000,007로 나눈 나머지를 출력한다.

# dp[n] = 2*dp[n-1] + 3*dp[n-2] + 2*(dp[n-3] + dp[n-4] + ... + dp[0])

"""
import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1 if n>3 else 4)
dp[0:3] = [1, 2, 7]

for i in range(3, n+1):
    dp[i] = (2 * dp[i-1] + 3 * dp[i-2]) % 1000000007
    for j in range(3, i+1):
        dp[i] += (2 * dp[i-j]) % 1000000007
print(dp[n])
"""
# 하지만 이렇게 구현하면 시간복잡도가 O(n)이므로 시간초과로 통과되지 않는다.
# 2*(dp[n-3]+dp[n-4]+...+dp[0]) 계산하는 과정이 중복된다는 사실을 알 수 있고 이 과정 또한 추가적인 배열을 사용함으로써 memoization으로 시간초과를 해결 할 수 있다.

# 하지만 배열 전체가 항상 필요한 것이 아니기 때문에 배열 대신 memo라는 변수를 추가해 문제를 해결하였다.

import sys

n = int(sys.stdin.readline())
dp = [0] * (n+1 if n>3 else 4)
dp[0:3] = [1, 2, 7]

memo = 0
for i in range(3, n+1):
    memo += dp[i-3]
    dp[i] = (2 * dp[i-1] + 3 * dp[i-2] + 2*memo) % 1000000007
print(dp[n])