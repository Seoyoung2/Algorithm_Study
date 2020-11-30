# https://programmers.co.kr/learn/courses/30/lessons/67256


from collections import deque


def bfs(here, hand, left, right):
    cnt = [[-1] * 3 for _ in range(4)]
    cnt[here[0]][here[1]] = 0
    q = deque([here])
    while q:
        x, y = q.popleft()
        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            if 0 <= x + dx < 4 and 0 <= y + dy < 3 and cnt[x + dx][y + dy] == -1:
                cnt[x + dx][y + dy] = cnt[x][y] + 1
                q.append((x + dx, y + dy))

    l = cnt[left[0]][left[1]]
    r = cnt[right[0]][right[1]]
    if l > r:
        return "R"
    elif r > l:
        return "L"
    else:
        return str.upper(hand[0])


def solution(numbers, hand):
    ans = ""
    left, right = (3, 0), (3, 2)
    cur = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for n in numbers:
        n = int(n)
        if n in [1, 4, 7]:
            ans += "L"
            left = cur[n]
        elif n in [3, 6, 9]:
            ans += "R"
            right = cur[n]
        else:
            tmp = bfs(cur[n], hand, left, right)
            ans += tmp
            if tmp == 'R':
                right = cur[n]
            else:
                left = cur[n]
    return ans