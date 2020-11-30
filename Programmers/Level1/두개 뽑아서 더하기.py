# https://programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    ans = set()
    for case in combinations(numbers, 2):
        ans.add(sum(case))
    return sorted(list(ans))