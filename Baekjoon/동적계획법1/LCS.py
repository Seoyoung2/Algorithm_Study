# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# LCS 알고리즘을 공부한 후 풀었다.
# LCS table의 형태는 다음과 같고 문자가 같을 경우, 왼쪽 대각선의 값에 1을 더한다.

# [[0, 0, 0, 0, 0, 0, 0],
# [0, 0, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 2, 2, 2],
# [0, 1, 2, 2, 2, 3, 3],
# [0, 1, 2, 2, 2, 3, 3],
# [0, 1, 2, 2, 2, 3, 4],
# [0, 1, 2, 3, 3, 3, 4]]


from sys import stdin

a = stdin.readline().strip()
b = stdin.readline().strip()

lcs = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])
