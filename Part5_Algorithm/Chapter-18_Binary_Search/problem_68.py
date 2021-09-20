"""
[Easy] 167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
import bisect
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


"""
위의 풀이대로 이진검색을 만드는 대신 bisect 모듈로 풀이를 진행하였다.
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, number in enumerate(numbers):
            diff_value = target - number

            diff_index = bisect.bisect_left(numbers[idx + 1:], diff_value)
            if len(numbers[idx + 1:]) > diff_index and numbers[diff_index + idx + 1] == diff_value:
                return idx + 1, diff_index + idx + 2


"""
슬라이싱을 하게되면 부분 리스트를 새롭게 생성한다는 문제점이 있다. 그러므로 리스트의 길이가 길면 길수록 슬라이싱을 사용하게되면 느려지게된다.

해당 문제는 bisect 모듈의 파라미터를 사용하여 개선했다.

참고: https://docs.python.org/ko/3/library/bisect.html
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, number in enumerate(numbers):
            diff_value = target - number

            diff_index = bisect.bisect_left(numbers, diff_value, idx + 1)
            if len(numbers) > diff_index and numbers[diff_index] == diff_value:
                return idx + 1, diff_index + 1


"""
슬라이싱을 하지 않을 때 약 10배 정도 속도가 빨라졌다. (1840 ms -> 134 ms)
코딩 테스트 실무에서 슬라이싱은 주의깊게 사용해야한다는 것을 배웠다.
"""
