"""
[Easy] 122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

"""
반복문으로 값의 차이가 0 보다 큰 경우 더해주기만 하면 해결할 수 있는 문제이다.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for idx in range(len(prices)-1):
            if prices[idx] < prices[idx + 1]:
                output += (prices[idx + 1] - prices[idx])
        return output

"""
이 문제가 왜 그리디 알고리즘인지에 대한 생각을 해봤다.
그리디 알고리즘으로 해결할 수 있는 문제는 
1. 탐욕 선택 속성을 갖고있고
2. 최적 부분 구조인 문제들이다. 

탐욕 선택 속성이란 앞의 선택이 이후 선택에 영향을 주지 않는 것을 말하고
최적 부분 구조란 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 경우를 말한다.

문제를 보면 1일째에 매수하고 2일째에 매도하여 수익을 내고 3일째 매수하고 2일째 매도하여 수익을 내더라도 앞의 선택이 이후의 선택에 영향을 주지 않는다.
그리고 수익을 내는 경우에 한해 계속 사고 하는 방법과 저점에 사서 고정에 파는 방법, 어느 방법도 항상 결과값은 같다.
그러므로 해당 문제는 그리디 알고리즘으로 푸는 경우라고 생각되어진다. 
"""