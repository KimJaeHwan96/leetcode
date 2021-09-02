"""
[Medium] 241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
from typing import List


"""
어떻게 문제를 풀지 어떻게 분할정복으로 풀이할지 고민을 했다. 아쉽게도 감이 안잡혀 답을 보면서 공부를 했다.
이 문제를 통해 분할정복과 재귀에 대한 감을 잡은 느낌이 든다.

우선 내 방식대로 내 생각대로 문제를 풀어봤다.
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, val in enumerate(expression):
            if val in '-+*':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                results.append(eval(str(left[0]) + val + str(right[0])))

        return results


"""
재귀는 헷갈리면 예제를 가지로 하나하나 그림을 그리면서 풀면 이해가 잘 된다.
이 풀이의 문제는 모든 경우의 수에 대한 값들이 계산되지 않는 다는것이다.
책의 풀이가 이해가 잘 안되어 내 방식대로 하다 왜 책의 풀이가 그렇게 됐는지 이해가 됐다.  
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, val in enumerate(expression):
            if val in '-+*':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                results.extend(compute(left, right, val))

        return results


"""
분할정복, 재귀로 구현할때 생각해야할것은 언제 리턴해서 루프를 끊어주느냐 라고 생각된다.
하지만 이 문제를 보먄 어떻게 리턴하냐 도 중요하다. 

if expression.isdigit():
    return [int(expression)] 

에서 expression 면 충분하다고 생각되었는데 하나하나 로직을 타다보면 이해가 된다.
재귀를 사용하면 구현한 같은 로직을 계속 타게 된다. 그러면 같은 로직이니 데이터 형식을 맞춰야 하고 부분 문제들을 해결한 후
각 부분 문제들을 모아 최종 답을 구하여 리턴하는 것도 같은 데이터 형식이 되어야한다.

물론 핵심은 각 경우의 수를 구하고 리스트에 저장하는 것이다.
그러므로 각 계산들은 리스트로 리턴을 해주고 리스트로 계산 및 구현을 한다.
"""


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for idx, val in enumerate(expression):
            if val in '-+*':
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx + 1:])
                results.extend(compute(left, right, val))

        return results
