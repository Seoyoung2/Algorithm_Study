# https://www.acmicpc.net/problem/10816

input()
nums = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
dic = {}

for n in nums:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
ans = []
for x in q:
    if x in dic:
        ans.append(dic[x])
    else:
        ans.append(0)
print(*ans)
