# https://www.acmicpc.net/problem/1517
# 버블 소트는 시간초과(O(n^2)) => 합병정렬(O(NlogN)) 사용
# 어려움.....


import sys
sys.setrecursionlimit(10**6)


def merge_sort(arr):
    global ans
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2

    # devide
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge
    cnt = 0
    res = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            # left의 원소가 새로운 배열(res)에 추가될 경우,
            # right에서 res로 먼저 채워진 수(cnt) 만큼 swap 진행
            res.append(left[l])
            l += 1
            ans += cnt
        else:
            # right의 원소가 새로운 배열(res)에 추가될 경우,
            # left에서 res로 채워지지 않은 left 원소 개수만큼 swap 진행
            res.append(right[r])
            r += 1
            cnt += 1
    while l < len(left):
        res.append(left[l])
        l += 1
        ans += cnt
    while r < len(right):
        res.append(right[r])
        r += 1
    return res


N = int(input())
A = list(map(int, input().split()))

ans = 0
merge_sort(A)
print(ans)
