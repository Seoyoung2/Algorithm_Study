# https://www.acmicpc.net/problem/2108

from collections import Counter

N = int(input())
nums = [int(input()) for _ in range(N)]

# 산술평균
print(round(sum(nums)/N))
# 중앙값
nums.sort()
print(nums[N//2])
# 최빈값
numb = Counter(nums).most_common()
print(numb)
if len(numb) > 1 and numb[0][1] == numb[1][1]:
    print(numb[1][0])
else:
    print(numb[0][0])
# 범위
print(nums[-1] - nums[0])
