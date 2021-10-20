"""
[medium] 78. Subsets
https://leetcode.com/problems/subsets/
"""
from typing import List


"""
모든 부분 집합을 구하는 문제이다.
핵심은
1. 모든 부분 집합을 저장한다. 즉, dfs 할 때 가장 먼저 부분집합으로 추가한다.
2. 인덱스를 1씩 증가하므로 탈출조건을 설정하지 않아도 모든 경우의 수를 구할 수있다.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            result.append(path)

            for idx in range(index, len(nums)):
                dfs(idx + 1, path + [nums[idx]])

        result = []
        dfs(0, [])
        return result