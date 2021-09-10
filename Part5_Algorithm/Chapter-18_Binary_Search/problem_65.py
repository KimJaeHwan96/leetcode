"""
[Easy] 704. Binary Search
https://leetcode.com/problems/binary-search/
"""
from typing import List

"""
처음 C 언어로 이진검색을 공부할 때와 같이 코드를 작성해보았다.  
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1

            mid = (left + right) // 2

            if nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return mid

        return binary_search(0, len(nums) - 1)


"""
실행시간은 394 ms 으로 많이 느리다. 가장 처음 볼만한 풀이로 이진검색을 이해하기에 가장 좋은 방법이다.
하지만 보통 이해만 하고 실제로 사용은 안할 것이다. 파이썬 빌트인 함수로 간단하게 풀이가 가능하기 때문이다.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1


"""
물론 이런 코드는 실무에서만 쓰고 코딩테스트 이므로 이런 풀이는 적절하지 않아보인다.
"""

