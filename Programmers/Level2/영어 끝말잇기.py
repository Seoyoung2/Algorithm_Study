# https://programmers.co.kr/learn/courses/30/lessons/12981


from collections import deque


def solution(n, words):
    turn = [[] for _ in range(n)]
    q = deque(words)
    i = 0
    while q:
        w = q.popleft()
        if turn[i - 1] and w[0] != turn[i - 1][-1][-1]:
            return [i + 1, len(turn[i]) + 1]
        for xs in turn:
            if w in xs:
                return [i + 1, len(turn[i]) + 1]
        turn[i].append(w)
        i = (i + 1) % n
    return [0, 0]


# best solution
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]