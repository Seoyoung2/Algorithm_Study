# https://www.acmicpc.net/problem/1541

from sys import stdin

slist = stdin.readline().rstrip()
S = []
idx = 0
for i in range(len(slist)):
    if slist[i] == '-':
        S.append(slist[idx:i])
        idx = i + 1
S.append(slist[idx:])

ans = eval(S[0])
for i in range(1, len(S)):
    ans -= eval(S[i])
print(ans)