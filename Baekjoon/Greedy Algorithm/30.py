# https://www.acmicpc.net/problem/10610

from sys import stdin

nlist = [int(n) for n in stdin.readline().rstrip()]
ans = 0
if 0 not in nlist or sum(nlist) % 3:
    ans = -1
else:
    nlist.sort(reverse=True)
    ans = "".join(map(str, nlist))

print(ans)