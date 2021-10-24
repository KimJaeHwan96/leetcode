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

"""
책에서 풀이한 코드는 아래와 같다. 똑같이 DFS 를 진행한다. 책의 풀이내용을 살짝 참고해서 여러개의 그래프나 나올 수 있기때문에 그래프의 각 Key 들을 DFS 해야한다는 것을 알았다.
이 코드를 실행하면 시간초과가 발생하는데 그 이유는 아래와 같다.

최악의 경우로 한 줄로 이루어진 그래프가 있다고 하자  1 -> 2 -> 3 -> ...... -> N - 1 -> N 와 같은 그래프가 있다고 하자
아래와 같은 코드의 경우 1인 노드를 시작점으로 N 인 노드 까지 DFS 를 하게된다. 그러면 시간복잡도 O(N^2)) 로 완전 탐색을 하게된다. 
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


"""
이를 방지하기 위해 방문한 노드를 저장하는 방법이 있다. 노드를 저장하는 시점은 이 노드는 더이상 순회할 필요가 없다는 것, 즉 순환하지 않는다는 것을 알았을 때 이다.
그러므로 탐색이 종료가 된 후인 traced.remove(i) 뒤에 visited.add(i) 을 하도록 한다.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


"""
내가 작성한 코드는 방문한 노드를 제거하며 가지치기를 하고 있어 굳이 방문한 노드를 저장할 필요없다.

while graph[course]:
    have_to_course = graph[course].popleft()

로 그전에 풀이한 방법과 비슷하게 pop 해버리고 dfs 를 재귀 호출하면 dfs 가 끝난 후에는 해당 노드와 연결된 그래프들을 순회했기 때문에 더이상 순회할 필요가 없다.
1 -> 2 -> 3 -> ...... -> N - 1 -> N 와 같은 그래프가 있다고 할때 1 인 노드을 시작점으로 순회하면서 방문한 노드들을 제거하므로 시간복잡도 O(N) 로 실행 가능하다. 

for y in graph[i]:
    if not dfs(y):

이와 같이 순회만 하게되면 중복 연산을 하게되므로 추가적으로 가지치기하는 연산이 필요하다. 그래서 방문한 노드들을 저장하는 로직을 추가하였다.
"""


"""
하나더 아주 알아두어야할 아주 중요한 점이있다.
defaultdict 는 Key 가 없으면 기본값으로 초기화를 해주어 반복문 수행시 에러가 발생한다.

for x in graph: 
와 같이 실행하면 RuntimeError 가 발생한다.

이를 해결하려면 새로운 복사본을 만들어야하므로 list 로 감싸야한다.
for x in list(graph):

새로운 복사본을 만들어야하므로 keys 도 에러가 발생한다.
for x in graph.keys():
"""