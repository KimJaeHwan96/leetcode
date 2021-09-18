"""
[Easy] 349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
"""
import bisect
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


"""
현 챕터가 이진 검색이므로 이진검색으로 풀이하는 방법을 고민해보았다.
우선 한 리스트를 정렬한 후 다른 리스트의 값들을 target 으로 생각하여 풀이하였다.ㅍ
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def binary_search(target):
            left, right = 0, (len(nums1) - 1)
            while left <= right:
                mid = left + (right - left) // 2
                if target < nums1[mid]:
                    right = mid - 1
                elif target > nums1[mid]:
                    left = mid + 1
                else:
                    return True
            return False

        # 한 리스트를 정렬
        nums1.sort()
        result = []
        for target_num in nums2:
            if binary_search(target_num) and target_num not in result:
                result.append(target_num)

        return result


"""
위 의 풀이를 최적화 한다면 list 대신 set 를 binary_search 대신 bisect 모듈을 사용하는 것이다.
시간은 크게 줄어들진 않지만 코드의 간결함이 늘어난다. 
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 한 리스트를 정렬
        nums1.sort()

        # 중복을 허용하지 않으므로 set 를 사용
        result = set()
        for target_num in nums2:
            # bisect 모듈 사용
            target_index = bisect.bisect_left(nums1, target_num)

            # bisect 를 사용할 경우 확인해야할 사항
            # 1. 리턴한 인덱스와 target 값을 비교
            # 2. 리턴한 인덱스가 찾으려는 리스트내에 있는지 확인
            if len(nums1) > target_index and nums1[target_index] == target_num:
                result.add(target_num)

        return result
