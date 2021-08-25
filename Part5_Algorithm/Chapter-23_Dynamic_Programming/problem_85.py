"""
[Easy] 509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""

"""
피보나치 수열은 프로그래밍을 처음 공부할 때 재귀로 푸는 것이 일반적이었다.
우선 재귀로 해결해 보았다.
"""


class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n

        return self.fib(n - 1) + self.fib(n - 2)


"""
간단하게 작성한 코드인데 성능은 그렇게 좋지 않다.
실행시간이 848 ms 으로 빠른 편이 아니다.
"""