"""
[Medium] 33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


"""
문제 해결방법을 정리해봤다.
1. 최솟값 찾기
2. pivot 찾기(최솟값의 인덱스가 pivot 이 된다.)
3. 이진 검색을 실행한다. (다만 mid 를 구한 후 pivot 을 더해야한다.)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 최솟값 찾아서 pivot 찾기
        min_num = min(nums)

        pivot = nums.index(min_num)
        # 기존에 left + (right - left) / 2 으로 mid 를 구한 후 mid + pivot 으로 원래 리스트의 중앙값을 가져옴
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1


"""
최솟값을 min 과 index 함수로 찾았는데 이진 검색으로 찾도록 개선을 해야한다.

테스트는 통과되지만 시간복잡도의 제약이 O(log n) 이기 떄문에 최소값도 이진 검색으로 찾아야한다. 
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 최솟값 찾아서 pivot 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        # pivot = right 도 똑같음
        pivot = left
        ...


"""
right 포인터를 기준으로 값을 비교하여 포인터를 이동시킨다.
이때 left 포인터를 기준으로 값을 비교하지 않는 이유가 있다.
right 포인터가 mid 포인터의 값보다 크다면 반드시 최소값이 [left: mid + 1] 에 있고
작다면 반드시 [mid: right] 에 있다.
하지만 left 포인터가 mid 포인터의 값보다 작다고 [left: mid] 에 있다는 보장이 없다. ex) [4,5,6,0,1,2,3]
그렇기 때문에 right 포인터의 값을 기준으로 포인터들을 이동시킨다.
"""
