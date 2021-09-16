"""
[Easy] 349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
"""
from collections import Counter
from typing import List

"""
Counter 끼리의 AND 연산으로 겹치는 값들을 리턴하면 간단히 해결가능해 보인다.
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        sum_counter = counter1 & counter2
        return [i[0] for i in sum_counter.most_common()]
