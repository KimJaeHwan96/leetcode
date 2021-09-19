"""
[Easy] 167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


"""
첫번째 풀이방법으로 순차적으로 숫자를 가져와서 target 과 그 숫자를 뺀 후 차이값을 이진검색으로 찾는 방법이다.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, number in enumerate(numbers):
            left, right = idx + 1, len(numbers) - 1
            diff = target - number
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < diff:
                    left = mid + 1
                elif numbers[mid] > diff:
                    right = mid - 1
                else:
                    return idx + 1, mid + 1


"""
두번째 방법으로는 투 포인터를 사용하는 방법이다.
left 와 right 포인터를 두고 두 인덱스의 값의 합을 구한다.
합의 값이 target 보다 크면 right 포인터를 왼쪽으로 옮기고 target 보다 작으면 left 포인터를 오른쪽으로 옮기는 풀이방법인다.  
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            expected_target = numbers[right] + numbers[left]
            if expected_target > target:
                right -= 1
            elif expected_target < target:
                left += 1
            else:
                return left + 1, right + 1
