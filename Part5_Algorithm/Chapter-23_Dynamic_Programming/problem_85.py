"""
[Easy] 509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""
from collections import defaultdict

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

"""
타뷸레이션이란 동적 프로그래밍의 방법론 중 상향식 접근법으로 미리 테이블에 저장하는 방식이다. 선형시간으로 리스트에 각 값을 저장하여 값을 구한다.
사용하지 않는 값도 저장한다는 단점이 있지만 일반 재귀보다 훨씬 빠르다.
"""


class Solution:
    def __init__(self):
        self.dict = defaultdict(int)
        self.dict[0] = 0
        self.dict[1] = 1

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        for i in range(2, n + 1):
            self.dict[i] = self.dict[i - 2] + self.dict[i - 1]

        return self.dict[n]

"""
메모이제이션란 동적 프로그래밍의 방법론 중 하향식 접근법으로 동일한 계산을 반복해야 할 경우 한 번 계산한 결과를 메모리에 저장해 두었다가 꺼내 씀으로써 중복 계산을 방지할 수 있게 하는 기법이다
이래는 메모이제이션으로 해결한 방법으로 재귀로 함수를 호출하지만 이미 값이 있다면 저장한 값을 꺼내온다.
타뷸레이션과 동일한 시간이 걸리고 마찬가지로 재귀보다 훨씬 빠르다.
"""


class Solution:
    def __init__(self):
        self.dict = defaultdict(int)
        self.dict[0] = 0
        self.dict[1] = 1

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dict[n]:
            return self.dict[n]

        self.dict[n] = self.fib(n - 2) + self.fib(n - 1)
        return self.dict[n]
