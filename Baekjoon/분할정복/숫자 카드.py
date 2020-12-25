# https://www.acmicpc.net/problem/10815

input()
nums = set(map(int, input().split()))
input()
q = list(map(int, input().split()))

ans = []
for n in q:
    if n in nums:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)