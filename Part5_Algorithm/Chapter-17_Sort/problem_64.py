"""
[Medium] 973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""

import heapq
from typing import List


"""
거리는 구하는 공식을 이용하여 가장 가까운 k 개의 점을 구하면 된다.
거리를 구할 때 루트 연산은 굳이 필요없어보여 코딩하지 않았고 가장 가까운 k 개는 우선순위 큐, heapq 모듈을 이용해서 풀이하면 된다고 판단했다.    
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for idx in range(len(points)):
            point = points[idx]
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (distance, point))

        return [heapq.heappop(heap)[1] for _ in range(k)]


"""
책의 풀이는 아래와 같다. 같은 풀이지만 가독성을 고려할 것이면 아래 코드가 더 좋아 보인다.
"""


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            distance = x ** 2 + y ** 2
            heapq.heappush(heap, (distance, x, y))

        result = []
        for _ in range(k):
            (distance, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result
