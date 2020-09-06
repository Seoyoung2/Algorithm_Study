# https://programmers.co.kr/learn/courses/30/lessons/60058


def split_uv(s):
    stk = [s[0]]
    i = 0
    for i in range(1, len(s)+1):
        if not stk:
            # tmp가 비었으면 거기까지가 u, 나머지는 v
            break
        elif s[i] != stk[-1]:
            stk.pop()
        else:
            stk.append(s[i])
    return s[:i], s[i:]


def right_str(s):
    stk = []
    for ch in s:
        if ch == "(":
            stk.append(ch)
        elif stk:
            stk.pop()
        else:
            return False
    return False if stk else True


def solution(p):
    if p == "" or right_str(p):
        return p
    u, v = split_uv(p)
    sv = solution(v)
    if right_str(u):
        return u + sv
    else:
        res = "(" + sv + ")"
        u = u[1:-1]
        next_u = ""
        for i in range(len(u)):
            if u[i] == "(":
                next_u += ")"
            else:
                next_u += "("
        res += next_u
        return res


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
