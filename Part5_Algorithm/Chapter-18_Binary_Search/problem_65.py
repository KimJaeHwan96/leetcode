"""
[Easy] 704. Binary Search
https://leetcode.com/problems/binary-search/
"""
from bisect import bisect_left
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
물론 이런 코드는 실무에서만 쓰고 코딩테스트에서 이런 풀이를 하는 것은 적절하지 않아보인다.

차라리 이진검색을 지원하는 bisect 모듈을 사용하는 것이 더 좋아보인다.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        target_idx = bisect_left(nums, target)

        if target_idx < len(nums) and nums[target_idx] == target:
            return target_idx
        else:
            return -1


"""
bisect 모듈은 이진 검색 그 자체를 지원한다기 보단 이진 검색을 통해 삽입을 위치를 알려준다. 그러므로 target 을 삽입할 위치를 리턴해준다.
리스트에 있는 값이 target 과 같다면 bisect_left 는 그 값의 인덱스를 리턴하고 bisect_right 는 그 값의 인덱스 + 1를 리턴한다.
그래서 bisect_left 를 사용해서 nums 에 target 의 위치를 리턴받았다. 하지만 이대로 끝난 것은 아니다.
nums 에 없는 값을 넣었을 경우에도 삽입할 인덱스를 리턴해주므로 값을 비교해주고(nums[target_idx] == target), 범위에 넘어선값이 있는지 검증한다.(target_idx < len(nums))
"""