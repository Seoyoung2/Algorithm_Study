# https://www.acmicpc.net/problem/6603

from sys import stdin
# from itertools import combinations
#
# while True:
#     num = list(map(int, stdin.readline().split()))
#     k = num[0]
#     if k == 0:
#         break
#     for case in combinations(num[1:], 6):
#         print(*case)
#     print()


# 위의 쉬운 방법이 있지만 DFS(+백트래킹)로 풀어보자..
def dfs(idx, cnt):
    # 6개 숫자 모두 뽑았으면 출력하고 끝내기
    if cnt == 6:
        print(*res)
        return
    # 숫자 더 뽑기
    for i in range(idx, k+1):
        # cnt번째 숫자로 nums[i] 뽑음
        res[cnt] = nums[i]
        dfs(i+1, cnt+1)


while True:
    nums = list(map(int, stdin.readline().split()))
    k = nums[0]
    if k == 0:
        break
    res = [0] * 6
    # nums[1]부터 탐색, cnt = 0
    dfs(1, 0)
    print()
