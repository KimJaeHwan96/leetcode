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
