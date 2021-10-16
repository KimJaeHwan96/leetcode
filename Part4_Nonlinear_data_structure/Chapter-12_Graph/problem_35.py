"""
[medium] 77. Combinations
https://leetcode.com/problems/combinations/
"""
from typing import List


"""
n 과 k 로 리스트를 만들고 문제를 풀이하는 방법으로 풀이할 생각을 했다.
다만 순열과 다른 점은 순서를 고려하지 않기때문에 좀더 간결하게 풀이 가능했다.
실행시간은 약 584 ms 이다. 
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(nums, combination):
            if len(combination) == k:
                result.append(combination)
                return

            for idx, num in enumerate(nums):
                dfs(nums[idx+1:], combination + [num])

        num_list = [num for num in range(1, n+1)]
        result = []
        dfs(num_list, [])
        return result


"""
n 과 k 를 그대로 이용하는 방법이다. 
리스트를 만들지 않기 때문에 좀더 간결하다. 다만 위는 만든 리스트를 슬라이싱 연산으로 복사하고 아래는 range 로 리스트를 생성한다.
슬라이싱 연산보다  range 가 더 무거운지 실행시간은 더 늦어졌다.
실행시간은 약 720 ms 이다.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(idx, combination):
            if len(combination) == k:
                result.append(combination)

            for i, num in enumerate(range(idx, n+1), start=idx):
                dfs(i + 1, combination + [num])

        result = []
        dfs(1, [])
        return result


"""
다음 풀이는 책의 풀이인데 순열과 비슷하게 인자를 이용하는 대신 값을 추가하고 빼는 연산으로 풀이했다.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
                return

            for num in range(start, n + 1):
                elements.append(num)
                dfs(elements, num + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result
