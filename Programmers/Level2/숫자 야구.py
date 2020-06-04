# 완전탐색 (https://programmers.co.kr/learn/courses/30/lessons/42841)


from itertools import permutations


def sb(num, i, strike, ball):
    s, b = 0, 0
    num = str(num)
    for n in range(3):
        if int(num[n]) == i[n]:
            s += 1
        elif int(num[n]) in list(i):
            b += 1
    return strike == s and ball == b


def solution(baseball):
    option = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for num, strike, ball in baseball:
        # option[:]을 씀으로써 remove해도 기존의 값을 유지하면서 for문 돌기 가능 !!!!!!!!!
        for i in option[:]:
            if not sb(num, i, strike, ball):
                option.remove(i)
    print(option)
    return len(option)


#  [세 자리의 수, 스트라이크의 수, 볼의 수] => 가능한 답의 개수 return
print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))   #2
print(solution([[123, 0, 0], [956, 0, 0]]))   #6
