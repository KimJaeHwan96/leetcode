"""
[Easy] 393. UTF-8 Validation
https://leetcode.com/problems/utf-8-validation/
"""
from typing import List


"""
어떻게 풀이할지에 대해서 고민했을 때 
1. 첫번째 값이 어떤값이냐에 따라 그 뒤의 값이 10xxx 으로 시작하는지를 검사해야한다. 
2. 10xxxx 인지 검사한 후 그 뒤의 값이 0xxx 인지 확인해야한다.

이부분을 어떻게 반복문으로 해결할지 감이 잘 오지 않았다. 
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def _check(index, check_count):
            for idx in range(index + 1, index + check_count + 1):
                if idx >= len(data) or format((data[idx] >> 6), 'b') != '10':
                    return False
            return True

        idx = 0
        while idx < len(data):
            number = data[idx]
            if format((number >> 3), 'b') == '11110' and _check(idx, 3):
                idx += 4
            elif format((number >> 4), 'b') == '1110' and _check(idx, 2):
                idx += 3
            elif format((number >> 5), 'b') == '110' and _check(idx, 1):
                idx += 2
            elif format((number >> 7), 'b') == '0':
                idx += 1
            else:
                return False
        return True


"""
책의 의도를 파악하면서 내 코드로 작성해였다.
10xxx 인지 검사, 0xxx 인지 검사 이 두 부분을 따로라고 생각했지만 검사하는 내부 메서드는 하나로 두는 게 좋아보였다.

게다가 쉬프트 한 후 이진수로 변환하는 데 0b 를 이용하면 굳이 이진수로 변환하지 않아도 되서 최적화가 가능하다.
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def _check(index, check_count):
            for idx in range(index + 1, index + check_count + 1):
                if idx >= len(data) or (data[idx] >> 6) != 0b10:
                    return False
            return True

        idx = 0
        while idx < len(data):
            number = data[idx]
            if (number >> 3) == 0b11110 and _check(idx, 3):
                idx += 4
            elif (number >> 4) == 0b1110 and _check(idx, 2):
                idx += 3
            elif (number >> 5) == 0b110 and _check(idx, 1):
                idx += 2
            elif (number >> 7) == 0b0:
                idx += 1
            else:
                return False
        return True
