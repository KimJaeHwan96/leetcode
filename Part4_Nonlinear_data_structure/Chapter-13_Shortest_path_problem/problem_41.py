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
