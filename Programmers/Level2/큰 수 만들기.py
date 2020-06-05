# Greedy (https://programmers.co.kr/learn/courses/30/lessons/42883)
# 짱 어려ㅜ움,,,,,,,,,,,,,,,,,,,,,,ㅠㅠ


def solution(number, k):
    length = len(number)
    m = 0
    for cnt in range(k):
        for idx in range(m, length-1):
            if number[idx] < number[idx+1]:
                number = number[:idx] + number[idx+1:]
                length -= 1
                if idx > 0:
                    m = idx-1
                break
        else:
            number = number[:length-k+cnt]
            break
    return "".join([str(i) for i in number])


print(solution("1924", 2))              #"94"
print(solution("1231234", 3))           #"3234"
print(solution("4177252841", 4))        #"775841"
print(solution("98769876", 3))        #"99876"
print(solution("55555", 3))        #"55"