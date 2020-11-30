# https://programmers.co.kr/learn/courses/30/lessons/42889


def solution(N, stages):
    ans1 = [0] * (N + 1)
    for x in stages:
        for y in range(x):
            ans1[y] += 1
    ans2 = [0] * N
    for i in range(N):
        ans2[i] = stages.count(i + 1)

    ans = []
    for i, x in enumerate(zip(ans1, ans2)):
        if x[0] == 0:
            ans.append((0, i + 1))
        else:
            ans.append((x[1] / x[0], i + 1))
    return list(x[1] for x in sorted(ans, key=lambda x: (-x[0], x[1])))


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))