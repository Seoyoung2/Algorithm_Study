# n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다.
# 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.
# 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.


from sys import stdin

n, k = map(int, stdin.readline().split())

data = []
for _ in range(n):
    data.append(int(stdin.readline()))

dp = [1] + [0] * k
for i in data:
    for j in range(i, k+1):
        dp[j] += dp[j-i]

print(dp[k])


# 점화식 찾아내는게 너무 어려워서 구글링 했다. 생각보다 간단한 코드였다,,

# 1. n가지 종류의 동전을 반복문으로 순회하면서 내부에서 반복문을 한 차례 더 돌린다.
# 2. 이 때 내부 반복문은 동전의 가치부터 k까지 순회한다.
# 3. 내부 반복문이 j번째를 순회한다고 했을 때 dp[j]에 dp[j-(순회중인 동전의 가치)]의 값을 더해준다.
