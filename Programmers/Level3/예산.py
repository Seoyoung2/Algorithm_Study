# https://programmers.co.kr/learn/courses/30/lessons/43237


def solution(budgets, M):
    L = len(budgets)
    if sum(budgets) <= M:
        return max(budgets)
    elif min(budgets) >= M:
        return M // L
    budgets.sort()
    mean = M // L
    for i in range(L):
        if budgets[i] < mean:
            M -= budgets[i]
        else:
            return M // (L - i)


print(solution([120, 110, 140, 150], 485))      #127