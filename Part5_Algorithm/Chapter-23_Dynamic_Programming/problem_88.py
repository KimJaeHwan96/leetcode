"""
[Medium] 198. House Robber
https://leetcode.com/problems/house-robber/
"""
from typing import List

"""
처음든 생각은 짝수 인덱스와 홀수 인덱스 끼리의 합으로 최대값을 구하면 되지 않을까 생각했다.
하지만 [8, 1, 1, 9] 인 경우 최대값은 17로 첫번째 집과 두 집 건너뛴 4번쨰 집의 합으로 구해진다. 그러므로 그렇게 간단하게 해결되진 않는다.

혹시 이 문제도 재귀로 풀 수 있지 않을까 생각이 들었다.
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])
        return _rob(len(nums) - 1)


"""
고민하다 생각이 잘 안나와 책의 아이디어와 코드를 참고하였다.
바로 어떻게 해결할지 머리 속에 안떠올라 아쉬웠다.
87번 문제와 동일하게 재귀를 사용하였고 동일하게 타임아웃이 발생했다.
"""



