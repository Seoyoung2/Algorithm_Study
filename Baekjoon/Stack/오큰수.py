# https://www.acmicpc.net/problem/17298
# 2중 for문으로 풀었더니 시간초과 => stack 사용, 로직이 어려움,,,,ㅠ.ㅠ

from sys import stdin

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

# for i in range(N):
#     for num in nums[i+1:]:
#         if num > nums[i]:
#             print(num, end=" ")
#             break
#     else:
#         print(-1, end=" ")

stack = []
ans = [-1 for _ in range(N)]
for i in range(N):
    # 스택의 top값보다 nums[i]이 더 클 경우 (오큰수)
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)
print(*ans)
