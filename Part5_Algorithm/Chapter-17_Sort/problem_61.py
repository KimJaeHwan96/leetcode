"""
[medium] 179. Largest Number
https://leetcode.com/problems/largest-number/
"""
from typing import List

"""
문제 해결방법으로 "정렬"을 해서 int list 를 string 으로 변환하는 방법이 있다.
여기서 문제는 정렬을 어떻게 해야할지 이다.

처음에는 각 int 를 string 으로 만들어 비교를 해야하나 고민했는데 간단하게 두 숫자의 자릿수를 변경하며 비교하면 됐다.
"""


class Solution:
    def is_swap(self, num1, num2):
        return int(str(num1) + str(num2)) < int(str(num2) + str(num1))

    def largestNumber(self, nums: List[int]) -> str:
        idx = 1

        while idx < len(nums):
            sorted_idx = idx

            while sorted_idx > 0 and self.is_swap(nums[sorted_idx - 1], nums[sorted_idx]):
                nums[sorted_idx], nums[sorted_idx - 1] = nums[sorted_idx - 1], nums[sorted_idx]
                sorted_idx -= 1

            idx += 1

        return str(int(''.join([str(num) for num in nums])))


"""
주의깊게 봐야할 곳, 개선할만한 곳이 두 곳있다.

1. int(str(num1) + str(num2)) < int(str(num2) + str(num1)) -> str(num1) + str(num2) < str(num2) + str(num1)

str 으로 자릿수를 변경하고 int 로 정수를 만들어 비교를 했는데 그럴 필요 없이 string 끼리도 비교가 가능하다.
숫자로 된 문자열 뿐만 아니라 알파벳과 한글도 가능하다. ord() 내장 함수를 사용하면 유니코드 코드 포인트를 반환한다.
참고: https://docs.python.org/ko/3/library/functions.html#ord 

2. str(int(''.join([str(num) for num in nums]))) -> str(int(''.join(map(str, nums))))
리스트 컴프리헨션보다 map 를 사용하는 것이 더 간결하다. (딱히 가독성을 해치지는 않는다.)
"""
