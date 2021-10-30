"""
[medium] 787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""
import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 그래프 구성
        graph = defaultdict(list)
        for _from, _to, _price in flights:
            graph[_from].append((_to, _price))

        Q = [(0, src, k + 1)]
        dist = defaultdict(int)
        while Q:
            time, node, k = heapq.heappop(Q)
            if k <= -1:
                continue

            if node not in dist or time < dist[node]:
                dist[node] = time
            for to, price in graph[node]:
                to_time = time + price
                heapq.heappush(Q, (to_time, to, k - 1))

        if dist[dst]:
            return dist[dst]
        return -1


"""
다익스트라 알고리즘을 응용하여 문제를 풀이해보았다. 하지만 타임아웃이 발생했다.
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k - 1))
        return -1


"""
책의 풀이 하지만 타임아웃이 발생했다... 어떤 부분이 문제인걸까? 최적화 할만한 부분을 찾아야한다.

리트 코드의 discuss 애서 찾은 코드가 있는데 잘 작동하여 수정만 살짝하여 가독성만 높였다.
참고: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686774/SUGGESTION-FOR-BEGINNERS-BFS-or-DIJKSHTRA-or-DP
"""


class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        if src == dst:
            return 0

        graph, seen = defaultdict(list), defaultdict(lambda: float('inf'))
        for u, v, p in flights:
            graph[u].append((v, p))

        Q = deque([(src, 0, -1)])
        while Q:
            print(Q)
            node, cost, k = Q.popleft()
            if node == dst or k == K:
                continue

            for to, p in graph[node]:
                if cost + p >= seen[to]:
                    continue
                seen[to] = cost + p
                Q.append((to, cost + p, k + 1))
        return seen[dst] if seen[dst] < float('inf') else -1


"""
타임 아웃이 발생한 코드와 제대로 동작한 코드사이의 차이점이 뭘까?
1. 우선순위 큐를 사용하는 지 여부 (heappush 가 append 보다 연산이 더 걸릴 것으로 판단)
2. 불필요한 연산이 많다

책의 풀이인 2번 풀이 와 heappush 연산과 리트코드 discuss 에서 가져온 3번 풀이의 append 연산을 수행횟수를 구했을때 각각 152 번 37번 수행됐다...

인자는 타임아웃이 발생한 테스트 케이스로 다음과 같았다.

n = 17
times = [[0, 12, 28], [5, 6, 39], [8, 6, 59], [13, 15, 7], [13, 12, 38], [10, 12, 35], [15, 3, 23], [7, 11, 26], [9, 4, 65], [10, 2, 38], [4, 7, 7], [14, 15, 31], [2, 12, 44], [8, 10, 34], [13, 6, 29],
 [5, 14, 89], [11, 16, 13], [7, 3, 46], [10, 15, 19], [12, 4, 58], [13, 16, 11], [16, 4, 76], [2, 0, 12], [15, 0, 22], [16, 12, 13], [7, 1, 29], [7, 14, 100], [16, 1, 14], [9, 6, 74], [11, 1, 73],
 [2, 11, 60], [10, 11, 85], [2, 5, 49], [3, 4, 17], [4, 9, 77], [16, 3, 47], [15, 6, 78], [14, 1, 90], [10, 5, 95], [1, 11, 30], [11, 0, 37], [10, 4, 86], [0, 8, 57], [6, 14, 68], [16, 8, 3],
 [13, 0, 65], [2, 13, 6], [5, 13, 5], [8, 11, 31], [6, 10, 20], [6, 2, 33], [9, 1, 3], [14, 9, 58], [12, 3, 19], [11, 2, 74], [12, 14, 48], [16, 11, 100], [3, 12, 38], [12, 13, 77], [10, 9, 99],
 [15, 13, 98], [15, 12, 71], [1, 4, 28], [7, 0, 83], [3, 5, 100], [8, 9, 14], [15, 11, 57], [3, 6, 65], [1, 3, 45], [14, 7, 74], [2, 10, 39], [4, 8, 73], [13, 5, 77], [10, 0, 43], [12, 9, 92],
 [8, 2, 26], [1, 7, 7], [9, 12, 10], [13, 11, 64], [8, 13, 80], [6, 12, 74], [9, 7, 35], [0, 15, 48], [3, 7, 87], [16, 9, 42], [5, 16, 64], [4, 5, 65], [15, 14, 70], [12, 0, 13], [16, 14, 52],
 [3, 10, 80], [14, 11, 85], [15, 2, 77], [4, 11, 19], [2, 7, 49], [10, 7, 78], [14, 6, 84], [13, 7, 50], [11, 6, 75], [5, 10, 46], [13, 8, 43], [9, 10, 49], [7, 12, 64], [0, 10, 76], [5, 9, 77],
 [8, 3, 28], [11, 9, 28], [12, 16, 87], [12, 6, 24], [9, 15, 94], [5, 7, 77], [4, 10, 18], [7, 2, 11], [9, 5, 41]]
src = 13
dst = 4
k = 13

"""
