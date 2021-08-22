"""
[Medium] 134. Gas Station
https://leetcode.com/problems/gas-station/
"""

"""
주유소를 방문하는 방향은 동일하므로 간단한 문제라고 생각되었다. 
문제 해결방법을 다음과 같이 정의했다.
1. gas, cost 리스트를 묶어 하나의 리스트로 묶는다.
2. gat 가 cost 보다 크거나 같은 최소 인덱스를 찾는다.
3. 모든 주유소를 방문 가능한지 계산한다.
4, 방문이 불가능하면 그 다음 인덱스를 선택한다.
5. 만약 보든 인덱스가 방문 불가능하면 -1 을 리턴한다.
"""


class Solution:
    def is_can_route_to_gas_stations(self, gas_stations, idx):
        count = 0
        remained_gas = 0
        while count <= len(gas_stations):
            gas_station = gas_stations[idx]
            remained_gas += gas_station[0] - gas_station[1]

            if remained_gas < 0:
                return False

            if idx + 1 >= len(gas_stations):
                idx = 0
            else:
                idx += 1
            count += 1
        return True

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_stations = []
        idx = 0
        while idx < len(gas) or idx < len(cost):
            gas_stations.append([gas[idx], cost[idx]])
            idx += 1

        for idx, gas_station in enumerate(gas_stations):
            gas = gas_station[0]
            cost = gas_station[1]
            if gas < cost:
                continue

            is_possible = self.is_can_route_to_gas_stations(gas_stations, idx)
            if is_possible:
                return idx

        return -1


"""
예상한대로 문제 해결은 가능했지만 최적화가 덜 되었다.
실행시간은 5388 ms 으로 확실히 오래 걸렸다. 
이중 반복문으로 O(n^2) 만큼 시간이 걸렸다.

최적화할 방법에 대해 고민해야한다. 
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start in range(len(gas)):
            fuel = 0
            for i in range(start, len(gas) + start):
                index = i % len(gas)

                can_travel = True
                if gas[index] + fuel < cost[index]:
                    can_travel = False
                    break
                else:
                    fuel += gas[index] - cost[index]

            if can_travel:
                return start
        return -1

"""
책의 풀이 방법인데 똑같이 이중 반복문을 사용하고있다. 내 코드보다 좀더 깔끔한 것 같으면서 읽기는 힘든 것 같다.
마찬가지로 모든 주유소를 방문하는데 모든 주유소에 대해 방문가능한지 확인한다. 비효울적이다.
"""

"""
책에서 구현한 최적화 코드

전체 gas 의 양이 cost 의 값보다 클경우 반드시 전체를 방문할 수 있는 출발점이 존재한다. (왜 이 생각을 못했는지 반성해야한다.. ㅠ)
이렇게 출발점이 없는 경우를 제외하면 반드시 하나가 존재하는 경우만 남게되어 반복문 하나로만 로직을 구현할 수 있다.
"""


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        return start

"""
반드시 출발점이 하나만 존재하므로 출발점을 앞에서 부터 찾으면 된다.
처음에는 각 출발점에서 방문이 가능한지 봐야하지 않을까 했지만, 출발점이 반드시 하나 존재한다는 제약이 구현을 쉽게 했다.
반복문 하나로 앞에서부터 검증을 하며 모두 방문이 불가능한 출발점을 제외하다보면 가능한 출발점이 나온다.
실행시간은 44 ms 으로 O(n^2) 와 O(n) 의 차이를 실감하게 되었다.
"""
