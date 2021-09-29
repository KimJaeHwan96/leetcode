"""
[medium] 56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        answer = []
        for interval in intervals:
            if not answer:
                answer.append(interval)

            prev = answer.pop()
            if prev[1] >= interval[0]:
                if prev[1] < interval[1]:
                    answer.append([prev[0], interval[1]])
                else:
                    answer.append([prev[0], prev[1]])
            else:
                answer.append(prev)
                answer.append(interval)
        return answer


"""
기본적인 로직은 이렇다
1. 앞 list[1]와 뒤 list[0]를 비교한다.
   1) 앞 list[1] > 뒤 list[0] => 병합 가능
   2) 앞 list[1] < 뒤 list[0] => 병합 불가능
2.  앞 list[1]와 뒤 list[1]를 비교한다.
    1) 앞 list[1] >= 뒤 list[1] => [앞 list[1], 앞 list[1]]
    2) 앞 list[1] < 뒤 list[1] => [앞 list[1], 뒤 list[1]]

중첩 if 문과 여러가지를 전부 따지면서 코드가 길어지고 가독성이 떨어진다.
게다가 intervals.sort()로 정렬은 되지만 책에는 첫번쨰 원소를 기준으로 하는 것을 보면 더 안전한듯 보인다.
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        answer = []
        for interval in intervals:
            if answer and answer[-1][1] >= interval[0]:
                answer[-1][1] = max(answer[-1][1], interval[1])
            else:
                answer += interval,
        return answer


"""
가독성이 그렇게 떨어지지 않는 범위에서 책의 내용을 이용해 리팩토링해봤다.
속도는 동일하지만 길이에서 차이가 난다.

answer += interval, 는
answer += [interval] 와 같은 의미로 중첩 리스트가 되게 한다.

a = [1], b =[2,3]
a += b
[1,2,3]

일반적으로 이렇게 되겠지만

a = [1], b = [2,3]
a += b,
or
a += [b]
[1,[2,3]]

이렇게 된다고 한다.
"""

"""
다시 풀면서 확인한 점

1. 사실 answer += interval, 이렇게 연산을 할 이유는 없다고 본다. answer.append(interval) 이렇게 하거나 차라리 answer += [interval] 로 코드를 작성하는 것이 더 낫아보인다.
2. 내가 풀이한 첫번째 풀이와 책에서 풀이한 두번째 풀이는 같다. 결국 앞 interval[1] 와 뒤 앞 interval[0] 을 비교하는 건데 첫번째 풀이는 너무 복잡하게 생각했다. 병합 여부만 판단하고 병합해야한다면 앞 interval[1] 값만 변경하면 된다. 
"""

