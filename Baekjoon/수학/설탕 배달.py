# https://www.acmicpc.net/problem/2839

N = int(input())

ans = 0
while N:
    if N % 5 == 0:
        ans += N // 5
        break
    N -= 3
    if N < 0:
        ans = -1
        break
    ans += 1
print(ans)

# 4 => -1