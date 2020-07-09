# https://www.acmicpc.net/problem/1541
# python의 eval()을 써서 문자열을 계산하려 했지만 "01"같은 문자열을 오류처리한다.
# "-"로 문자열을 나눈 후, 문자열의 첫 원소는 더하고 나머지는 빼는 방법("+"로 문자열을 나눠서 계산진행)


from sys import stdin

slist = stdin.readline().rstrip().split("-")
ans = 0
for i in range(len(slist)):
    for num in map(int, slist[i].split("+")):
        if i == 0:
            ans += num
        else:
            ans -= num
print(ans)