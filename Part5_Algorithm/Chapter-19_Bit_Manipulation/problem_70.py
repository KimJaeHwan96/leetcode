"""
[Easy] 136. Single Number
https://leetcode.com/problems/single-number/
"""
from collections import Counter
from typing import List


"""
하나의 원소를 제외한 모든 원소는 2개씩 있다.
원소의 개수를 찾기에는 Counter 을 사용하면 금방 푼다.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for num in nums_counter:
            if nums_counter[num] == 1:
                return num


"""
비트 조작으로 해결할 수 있는 방법이 있는지? 에 대해서 고민을 안해버리고 Counter 를 사용할 생각만 했는데 
XOR 로 해결하는 문제 풀이가 있었다.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer


"""
처음 봤을때는 감탄만 나왔다. 어떻게 이런생각을 할 수 있을지
물론 쉬운 문제이고 제약사항이 명확하지만 평소에 비트 연산에 대한 이해가 머리속에 남아있어야 가능하다고 생각된다.
비트 연산자를 어떻게 사용할지 고민이 필요하다.
"""