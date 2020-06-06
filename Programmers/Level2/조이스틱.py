# Greedy (https://programmers.co.kr/learn/courses/30/lessons/42860)


def solution(name):
    answer = 0
    name = list(name)
    index = 0
    while True:
        right = 1
        left = 1
        # updown count
        if name[index] != 'A':
            answer += min(ord(name[index])-ord('A'), ord('Z')-ord(name[index])+1)
            name[index] = 'A'
        # complete
        if name == ["A"]*len(name): break
        # 현재 위치에서 가장 가까운 "A"가 아닌 알파벳으로
        for i in range(1, len(name)):
            if name[index+i] == "A": right += 1
            else: break
        for i in range(1, len(name)):
            if name[index-i] == "A": left += 1
            else: break
        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer


print(solution("JEROEN"))               #56
print(solution("JAN"))                  #23
print(solution("AABAAAAAAB"))           #6
print(solution("AAAAAAA"))              #0
print(solution("ABBBBAAAAABAAA"))       #15
print(solution("ABBBBAAAAABA"))       #13