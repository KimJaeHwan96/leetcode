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


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num = float('-inf')
        window = deque()
        result = []
        for idx, num in enumerate(nums):
            window.append(num)
            if idx < k - 1:
                continue

            if max_num == float('-inf'):
                max_num = max(window)
            elif num > max_num:
                max_num = num

            result.append(max_num)
            if max_num == window.popleft():
                max_num = float('-inf')

        return result


"""
책을 통해서 얻은 큐를 이용한 힌트와 풀이를 보고 문제를 풀어봤다.
놀랍게도 똑같이 timeout 이 발생했다.

https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        bigger = deque()
        for idx, num in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] <= num:
                bigger.pop()

            # add in
            bigger.append(idx)

            # make sure the leftmost one is in-bound
            if idx - bigger[0] >= k:
                bigger.popleft()

            # if idx + 1 < k, then we are initializing the bigger array
            if idx + 1 >= k:
                res.append(nums[bigger[0]])
        return res
