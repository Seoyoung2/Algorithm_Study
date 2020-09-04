# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    if len(s) == 1:
        return 1
    ans = []
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        res = ""
        first = s[:i]
        for j in range(i, len(s)+i, i):
            if first == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += first
                else:
                    res += str(cnt) + first
                first = s[j:j+i]
                cnt = 1
        ans.append(len(res))
    return min(ans)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))

