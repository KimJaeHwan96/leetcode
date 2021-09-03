"""
[Hard] 239 Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""
from collections import deque
from typing import List

"""
구현 자체는 쉬워보여 간단하게 풀이해 보았다.
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx = 0
        result = []
        while idx + k - 1 < len(nums):
            num = max(nums[idx: idx + k])
            result.append(num)
            idx += 1

        return result


"""
책에서는 704ms 가 발생했다고 했지만 내가 실행했을때는 타임아웃이 발생했다.
제약사항에서 nums 의 길이가 10만이기 때문이라고 생각된다.
"""
