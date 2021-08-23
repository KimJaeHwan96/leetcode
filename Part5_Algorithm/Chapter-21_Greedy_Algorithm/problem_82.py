"""
[Easy] 455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
"""

"""
정렬한 후, 쿠키와 아이를 하나씩 비교하면서 몇명까지 가능한지 구하면 되는 문제이다.
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        child_idx = 0
        cookie_idx = 0
        while child_idx < len(g) and cookie_idx < len(s):
            if g[child_idx] <= s[cookie_idx]:
                child_idx += 1
            cookie_idx += 1

        return child_idx


"""
우선순위 큐로 구하는 방법이 있지 않을까 고민했었는데 책에서 이진탐색에 대한 힌트를 주었다.
쿠키의 크기가 중복될 수 있어서 우선순위 큐 보다는 이진탐색이 낫지 않을까 생각이 들었다. 
어차피 리스트를 heapq.heapify 하거나 s.sort() 를 하거나 속도는 비슷하기 때문에 이진탐색이 더 적합하다고 생각된다.
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
        return result

"""
책에서 본 풀이이다. collections, heapq 에 이어서 bisect 모듈도 공식문서를 볼 필요성이 생겼다.
"""