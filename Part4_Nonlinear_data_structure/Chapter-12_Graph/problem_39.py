"""
[medium] 207. Course Schedule
https://leetcode.com/problems/course-schedule/
"""
from collections import defaultdict, deque
from typing import List

"""
[a, b] 형식의 리스트로 나타내고 a를 진행하려면 b를 먼저 진행해야한다는 뜻이다. 이를 그래프로 표현하면 b -> a 로 표현가능할 것같다.
저 리스트들도 그래프로 만들어서 DFS 하면 될것이라고 판단된다.
path 를 저장하며 혹시 순환 그래프인 경우 False, 순환 그래프가 아닌 경우 True 를 리턴하면 될 듯 싶다.

[[1,2], [3,2]] 같은 경우도 입력값으로 주면 어떻게 DFS 로 순환인지 아닌지 판단할 것인지,...

"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(deque)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])

        def dfs(course):
            if course in route:
                return False

            route.add(course)
            while graph[course]:
                have_to_course = graph[course].popleft()
                if not dfs(have_to_course):
                    return False
            route.remove(course)
            return True

        route = set()
        for course in list(graph):
            if not dfs(course):
                return False
        return True


"""
1. 리스트 대신 set 를 사용한 이유 -> 각 노드들이 고유하고 순환하는 지만 체크하기 때문
2. 그전 문제 풀이 처럼 dfs 인자에 하나의 값만 넣지 않고 graph 의 key 들을 순회해서 dfs 하는 이유 -> [[1,0], [2, 3]] 과 같이 연결이 되지 않아도 되기 때문에 각각의 노드별로 체크를 해야함
3. dfs > 반복문 끝난 후에 remove 하는 이유 -> [[1,4],[2,4],[3,1],[3,2]] 을 예로 들겠다. dfs 하면 3 -> 1 -> 4 로 순회를 하고 3 -> 2 -> 4 를 순회 하게된다. removce 를 하지 않으면 route 에는 3, 1, 4 를 포함한 채로
3 -> 2 -> 4 순회할 때 route 에는 3, 1, 4 가 있으므로 에러를 뱉는다. 3 -> 1 -> 4 와 3 -> 2 -> 4 는 별개로 보면 될것같다.
"""
