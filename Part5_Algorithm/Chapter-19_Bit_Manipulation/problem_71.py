"""
[Easy] 461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
"""


"""
처음에는 각 숫자를 binary 로 변환하고 다른 값을 카운트 하는 방법을 생각했다.
하지만 숫자가 차이가 나면 비트의 수가 맞춰지지 않아 맞춘수 비교를 해야한다.

XOR 을 이용하면 간단하게 해결이 가능해보여 풀이하였다.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # binary_distance = bin(x ^ y)
        binary_distance = format(x ^ y, 'b')
        return binary_distance.count('1')


"""
bin 함수로 숫자를 변환하면 '0b0101' 이렇게 나오기 때문에 0b 를 없애려면 format 을 사용해야한다. 
"""