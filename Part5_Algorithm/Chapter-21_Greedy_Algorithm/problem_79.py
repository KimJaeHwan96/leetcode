"""
[Medium] 406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/
"""
import heapq

"""
가장 먼저 반목문을 통해 리스트에 삽입하는 방법을 고민했다.
하나씩 비교하며 어느 위치에 넣야할지 비교를 하는 방법이다.
하지만 과연 이게 효율적인지?, 옳은 방법인지 의구심이 들었다.
"""

"""
어떻게 그리디 알고리즘으로 풀어야할지 고민하던중에 책에서 어떠한 규칙이 있고 우선순위 큐로 풀이하면 해결이 된다는 것을 보았다
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            # heapq 는 최대힙을 지원하지 않으므로 -로 저장
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        # for 문 대신 while 문이 더 어울린다.
        # for _ in range(len(people)):
        while heap:
            human = heapq.heappop(heap)
            result.insert(human[1], [-human[0], human[1]])

        return result
"""
해당 코드는 책에서 한번 이해하고 다시 작성해본 코드이다. 사실 어떤 규칙이 있는 지 잘 모르겠고, 그래서 어떻게 우선순위 큐를 활용할지 몰랐다.
그리디 알고리즘으로 해결하는 문제이지만 먼저 규칙을 살펴야하는 문제이므로 많이 헤멨다.

가장 키(h)가 큰 순서대로 값을 꺼내 k 번쨰 인덱스에 insert 하면 해결되는 문제인데 다른 해결방법이나 어떻게 규칙을 빠르게 찾을지 고민이 필요해보인다.
"""