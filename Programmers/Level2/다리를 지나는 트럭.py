# 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
# ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
# solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
# 제한 조건 :
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    ans = 0
    sum_weight = 0
    bridge = deque([0] * bridge_length)
    while bridge:
        ans += 1
        sum_weight -= (bridge.popleft())
        if truck_weights:
            if sum_weight + truck_weights[0] <= weight:
                sum_weight += truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return ans

# deque는 그냥 list에서 pop(0)을 해도 되지만 그냥 써봄 : popleft()
# 처음에 bridge 위에 있는 트럭들의 총 무게를 sum()함수(O(n))를 사용했으나 시간초과. -> 변수로 할당해서 해결
print(solution(2, 10, [7,4,5,6]))                           #8
print(solution(100, 100, [10]))                             #101
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))  #110