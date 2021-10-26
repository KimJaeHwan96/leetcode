"""
[medium] 743. Network Delay Time
https://leetcode.com/problems/network-delay-time/
"""
import heapq
from collections import defaultdict
from typing import List

"""
모든 노드가 신호를 받을 수 있는가?
-> 각 경로를 업데이트하여 총 노드의 수 인 N 과 같은지 확
모든 노드가 신호를 받을때 까지의 시간은?
-> 가장 오래걸리는 노드까지의 시간, 즉 시작점부터 특정 노드까지의 시간을 구한 뒤 그중 가장 큰 시간을 구하면 된다.
"""


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        times: [[u, v, w]] (u: 출발노드 v: 도착노드, w: 가중치)
        k: 시작노드(start node)
        n: 노드 개수 (total node)
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        Q = [(0, k)]
        # 시작점이 k 인 그래프의 거리 데이터 저장
        dist = defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    time_to_v = time + w
                    heapq.heappush(Q, (time_to_v, v))

        if len(dist) == n:
            return max(dist.values())
        return -1
