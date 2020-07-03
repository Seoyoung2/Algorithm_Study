# https://www.acmicpc.net/problem/6603

from sys import stdin
from itertools import combinations

while True:
    nums = list(map(int, stdin.readline().split()))
    k = nums[0]
    if k == 0:
        break
    for n in combinations(nums[1:], 6):
        for i in n:
            print(i, end=" ")
        print()
    print()
