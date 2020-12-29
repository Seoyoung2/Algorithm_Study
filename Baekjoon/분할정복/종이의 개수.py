# https://www.acmicpc.net/problem/1780

def divide_paper(dp):
    ldp = len(dp)
    row = ldp // 3
    for i in range(0, ldp, row):
        for j in range(0, ldp, row):
            check_paper([a[j:j+row] for a in dp[i:i+row]])


def check_paper(cp):
    lcp = len(cp)
    chk = cp[0][0]
    for i in range(lcp):
        for j in range(lcp):
            if cp[i][j] != chk:
                divide_paper(cp)
                return
    ans[chk+1] += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
ans = [0] * 3
check_paper(paper)

for a in ans:
    print(a)

