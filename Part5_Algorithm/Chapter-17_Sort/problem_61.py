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


"""
다른 사람의 풀이를 보다가 위 풀이보다 깔끔하고 우아한 풀이 방법이 있다는 것을 발견했다.
매직 메서드를 이용하는 것이다.
코드 참고: https://leetcode.com/problems/largest-number/discuss/53162/My-3-lines-code-in-Java-and-Python/54346
"""


class Comparable:
    def __init__(self, num):
        self.value = str(num)

    def __lt__(self, other):
        print('__lt__ :', self.value, other.value)
        return self.value + other.value > other.value + self.value

    # def __gt__(self, other):
    #     print('__gt__ :', self.value, other.value)
    #     return self.value + other.value < other.value + self.value
    #
    # def __eq__(self, other):
    #     print('__eq__ :', self.value, other.value)
    #     return self.value + other.value == other.value + self.value


class Solution:
    def largestNumber(self, nums):
        num_strings = [Comparable(n) for n in nums]
        num_strings.sort()
        print([num.value for num in num_strings])
        output = ''.join(map(lambda x: x.value, num_strings))
        return output.lstrip('0') or '0'


"""
정렬을 할때 __lt__ 매직메서드만 이용하면 정렬이 가능하다.
value 가 int 임을 가정할 때 __lt__ 메서드가 return self.value > other.value 이면 내림차순, return self.value < other.value 이면 오름차순이다.
그래서 value 를 str 으로 변환시키고 return self.value + other.value > other.value + self.value 으로 내림차순을 실행한다.

비교는 a = 1 이고 b = 2 이면서 a > b 연산을 한다고 가정해보자

a < b ->  operator.__lt__(a, b) 으로  a < b 은 사실 int.__lt__(a, b) 연산이다. 
(a.__lt__(b) -> int.__lt__(a, b) 으로 a < b 과 a.__lt__(b) 의 결과는 같지만 사실 실행코드가 다르다.)

비교 매직베서드에 관한 설명: https://docs.python.org/ko/3/reference/datamodel.html#customization
__lt__ 메서드만 존재하면 정렬할 수 있음: https://docs.python.org/ko/3/library/functions.html#sorted
정렬 방법: https://docs.python.org/ko/3/howto/sorting.html#sortinghowto
"""