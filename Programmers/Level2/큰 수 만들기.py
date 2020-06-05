# Greedy (https://programmers.co.kr/learn/courses/30/lessons/42883)


def solution(number, k):
    tmp = list(number)
    idx = tmp.index(max(tmp[:k]))
    tmp = tmp[idx:]
    cnt = 0
    i = 0
    while True:
        if tmp[i] < tmp[i+1]:
            tmp.remove(str(tmp[i]))
            cnt += 1
        if cnt == k-idx:
            break
        i += 1
    return "".join(tmp)


print(solution("1924", 2))              #"94"
print(solution("1231234", 3))           #"3234"
print(solution("4177252841", 4))        #"775841"
print(solution("98769876", 3))        #"99876"