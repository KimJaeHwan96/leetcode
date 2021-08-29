"""
[Easy] 70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""
from collections import defaultdict

"""
각 계단을  1계단 또는 2계단으로만 오르니 재귀로 해결가능하지 않을까 고민했다.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)


"""
재귀를 생각하여 작성하니 피보나치 수열의 느낌을 받았다. 그러다보니 그전에 해결했던 메모이제이션과 타뷸레이션으로 해결하는 방법이 생각나 풀이해보았다.
"""


# 메모이제이션
class Solution:
    def __init__(self):
        self.table = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if self.table[n]:
            return self.table[n]

        self.table[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.table[n]


# 타뷸레이션
class Solution:
    def __init__(self):
        self.table = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        for step in range(0, n + 1):
            if step <= 2:
                self.table[step] = step
            else:
                self.table[step] = self.table[step - 1] + self.table[step - 2]
        return self.table[n]
