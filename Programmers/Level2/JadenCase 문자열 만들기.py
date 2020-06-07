# https://programmers.co.kr/learn/courses/30/lessons/12951


def solution(s):
    answer = [s[0].upper()]
    for i in range(1, len(s)):
        if s[i] == " ":
            answer.append(" ")
        elif s[i] != " " and s[i-1] == " ":
            answer.append(s[i].upper())
        else:
            answer.append(s[i].lower())
    return "".join(answer)


print(solution("3people unFollowed me"))        #"3people Unfollowed Me"
print(solution("for the last week"))        #"For The Last Week"
print(solution("for   the last week"))        #"For The Last Week"