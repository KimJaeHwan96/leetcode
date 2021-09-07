"""
[Easy] 191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""


"""
다른 문제와 비슷하게 binary 로 변환한 후 1의 개수를 찾는 코드로 풀이하였다.
간단하게 해결 가능하다.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_n = format(n, 'b')
        return binary_n.count('1')


"""
하지만 비트조작으로 풀이하는 방법을 고민하는게 좋아보인다. 
어떻게 1의 개수를 알 수 있을지... 생각이 잘 안났다.
책의 풀이를 보면서 비트 연산을 연습하는 것이 중요해보인다고 생각이 들었다.
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


"""
이 풀이의 기본 바탕은 숫자 A 를 A - 1 한 값을 AND 연산을 하면 비트가 1씩 빠진다. 
1111 & 1110 = 1110 으로 1인 비트가 없어진다.

해당 풀이가 마음에 드는 이유는 범용적이기 때문이다. 
게다가 첫 번째 풀이는 누구나 할 수 있겠지만 두 번째 풀이는 아무나 할 수 없어 보인다.
"""