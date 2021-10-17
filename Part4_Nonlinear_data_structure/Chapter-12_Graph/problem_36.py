"""
[medium] 39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""
from typing import List

"""
target 이 되는 원소를 구하는 데 핵심은 중복이 가능하다는 것과 순서는 무시하는 것이다.
중복: dfs 로 재귀호출할 때 자기자신도 포함해서 호출하면 된다.
순서 무시: 리스트는 현재 원소에서 자기자신 포함하면 된다. (자신의 앞에 있는 원소는 포함하지 않는다.)
이 내용으로 풀이하면 아래와 같다.
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidate_list, path, candidate_sum):
            if candidate_sum < 0:
                return
            if candidate_sum == 0:
                result.append(path)
                return

            for idx, candidate in enumerate(candidate_list):
                dfs(candidate_list[idx:], path + [candidate], candidate_sum - candidate)

        result = []
        dfs(candidates, [], target)
        return result


"""
만약 조합이 아니라 순열이었으면 재귀 호출할 때마다 전체 리스트를 순회하도록하면 구할 수 있다.
"""
