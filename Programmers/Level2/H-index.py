# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

# 제한사항:
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 나의 풀이 : filter()를 써봄, 주어진 배열 길이부터 0으로 내려오면서 검사
def solution(citations):
    l = len(citations)
    for i in reversed(range(l+1)):
        oo = filter(lambda x:x>=i, citations)
        if len(list(oo)) >= i:
            return i

# 주어진 배열을 정렬하면 citations[i-1], citations[i-2]에는 이미 citations[i]보다 큰 값이 들어있다는 사실
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 걍 신기: [(1,6),(2,5),(3,3),(4,1),(5,0)] -> [1, 2, 3, 1, 0] -> 3
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
