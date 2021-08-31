"""
[Medium] 198. House Robber
https://leetcode.com/problems/house-robber/
"""
from collections import OrderedDict
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


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)

        num_list = []
        num_list.append(nums[0])
        # num_list.append(nums[1])
        num_list.append(max(nums[0], nums[1]))

        for idx in range(2, len(nums)):
            max_num = max(num_list[idx - 1], num_list[idx - 2] + nums[idx])
            num_list.append(max_num)

        return max(num_list)

"""
다이나믹 프로그래밍으로 해결할 방법을 고민해봤다. 책에서 힌트를 얻었다.
타뷸레이션으로 해결할 방법을 고민하다 그전 문제와 같이 해결하려고 했다. 1번째 값과 2번쨰 값의 최대값은 각각의 값이라고 생각하고 풀었다.
하지만 [2,1,1,2] 인경우 답은 3이 아닌 4이다. 이부분을 어떻게 해결할까 고민하다 책의 해답을 보며 해결했다.
잘 생각해보면 num이 하나 있을때 는 그 값이 최대 값이다.
num 이 2개 있을때는 2개중 더 큰 값이 최대값이다. 3개 있을때는 3개 중 인접하지 않는 값들을 더해 각 값들의 합이 된다.
이런 식으로 나아가다 보면 규칙이 보인다. 최적 부분 구조가 보이고 하위 문제들이 중복되어있다.
"""

"""
책을 다시 보니 고칠부분이 보인다.
for idx in range(2, len(nums)):
    max_num = max(num_list[idx - 1], num_list[idx - 2] + nums[idx])
    num_list.append(max_num)

이런식으로 최대값을 구하다보면 리스트의 끝에 있는 값이 최대값이 된다.
max(num_list) -> num_list[-1] 으로 고치면 더 빠르게 동작한다.

책의 해답을 보니 리스트보다 OrderedDict 를 사용하는 방법도 있는 것을 깨달았다. 
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return max(nums)

        dp = OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])
        return dp.popitem()[1]

"""
책에서는 28ms 가 나왔지만 실행결과 58~61 ms 이 나왔다.
원래 OrderedDict 가 느리면 리스트가 더 낫지 않을까 생각이 든다.
"""
