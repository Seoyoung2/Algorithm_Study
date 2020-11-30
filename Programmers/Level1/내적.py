# https://programmers.co.kr/learn/courses/30/lessons/70128

from operator import mul


def solution(a, b):
    tmp = map(mul, a, b)
    return sum(tmp)