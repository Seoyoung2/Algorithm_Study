# https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    ans = ""
    while n:
        rem = n % 3
        n = n // 3
        ans = str(rem) + ans
    ans = str(ans)[::-1]
    return int(ans, 3)