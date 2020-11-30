# https://programmers.co.kr/learn/courses/30/lessons/17681


def solution(n, arr1, arr2):
    map1, map2 = [0] * n, [0] * n
    for i, ar in enumerate(arr1):
        tmp = bin(ar)[2:]
        map1[i] = '0' * (n - len(tmp)) + tmp
    for i, ar in enumerate(arr2):
        tmp = bin(ar)[2:]
        map2[i] = '0' * (n - len(tmp)) + tmp

    ans = [""] * n
    for i in range(n):
        for j in range(n):
            if map1[i][j] == map2[i][j] and map1[i][j] == '0':
                ans[i] += " "
            else:
                ans[i] += "#"
    return ans


def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer