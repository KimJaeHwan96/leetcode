"""
[medium] 332. Reconstruct Itinerary
https://leetcode.com/problems/reconstruct-itinerary/
"""
import collections
from collections import deque, defaultdict
from typing import List

"""
입력된 리스트를 디셔너리 객체로 표현한 그래프로 변환한 후 DFS 를 하면 답을 구하지 않을까 생각이 든다.


[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

convert to

{
    "JFK": ["SFO", "ATL"],
    "SFO": ["ATL"],
    "ATL": ["JFK", "SFO"]
}

다음과 겉이 변환한 후 해당 그래프를 DFS 하면서 일정을 구하면 될 것같다.
문제는 답이 여러개 나올 수 있고 여러 개의 답 중에 사전 순서가 오름차순으로 정렬된 값이 정답이라는 한가지 제약때문에 조건을 추가해야 할 것같다.
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(from_itinerary):
            while graph[from_itinerary]:
                to_itinerary = graph[from_itinerary].popleft()
                dfs(to_itinerary)
            path.append(from_itinerary)

        graph = defaultdict(deque)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)

        path = []
        dfs('JFK')
        return path[::-1]


"""
사실 DFS 를 이용하여 구한다는 것은 그래프 문제이고 그전까지 그렇게 풀어왔던 관성 때문이다.
모든 정점를 지나는 여행일정을 만들어야하고 사전순서대로 해야하기때문에 어떻게 순서대로 각 정점들을 지나면서 경로를 저장할 것인가가 문제가 된다.
경로를 순서대로 기록한다는 관점에서 보면 하나의 문제점이 있다. 
[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 를 예로 들어보면 JFK 다음에 사전순서의 앞에 있는 KUL 로 가야한다. 하지만 KUL 로 가면 나머지 정점을 지나갈 수 없기 때문에 NRT 부터 지나야한다.
즉, 지나가려는 정점이 막다른 정점인지에 대한 확인이 필요하다.

그렇기 때문에 DFS 를 이용하여 풀이한다.
while graph[from_itinerary]:
    to_itinerary = graph[from_itinerary].popleft()
    dfs(to_itinerary)

지나갈 수 있는 정점이 있는한 계속 재귀호출한다.

path.append(from_itinerary)
그리고 더이상 지나갈 정점이 없는 경우 경로에 추가한다. 그렇기 때문에 [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] 예 에서 막다른 정점인 KUL 이 가장 먼저 경로에 추가가 된다. 
위의 로직들로 모든 정점을 지나는지 확인할 필요가 없다. 더이상 지나갈 정점이 없는 경우 경로에 추가하기만 하면 된다.
"""


"""
재귀로 해결가능하니 반복문으로도 풀이가능하다.
stack 을 이용하여 DFS 를 하였고 더이상 연결된 노드가 없으면 경로에 넣도록 했다. 위와 구현은 비슷하다.
"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(collections.deque)
        for _from, _to in sorted(tickets):
            graph[_from].append(_to)

        path = []
        stack = ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].popleft())
            path.append(stack.pop())

        return path[::-1]
