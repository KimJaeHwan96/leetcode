"""
[Hard] 239 Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/
"""
from collections import deque
from typing import List

"""
구현 자체는 쉬워보여 간단하게 풀이해 보았다.
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        idx = 0
        result = []
        while idx + k - 1 < len(nums):
            num = max(nums[idx: idx + k])
            result.append(num)
            idx += 1

        return result


"""
책에서는 704ms 가 발생했다고 했지만 내가 실행했을때는 타임아웃이 발생했다.
제약사항에서 nums 의 길이가 10만이기 때문이라고 생각된다.
"""


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_num = float('-inf')
        window = deque()
        result = []
        for idx, num in enumerate(nums):
            window.append(num)
            if idx < k - 1:
                continue

            if max_num == float('-inf'):
                max_num = max(window)
            elif num > max_num:
                max_num = num

            result.append(max_num)
            if max_num == window.popleft():
                max_num = float('-inf')

        return result


"""
책을 통해서 얻은 큐를 이용한 힌트와 풀이를 보고 문제를 풀어봤다.
놀랍게도 똑같이 timeout 이 발생했다.

https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)
리트코드의 다른 풀이를 보고 타임아웃이 발생하지 않는 코드를 찾아봤다.
"""


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        window = deque()
        for idx, num in enumerate(nums):
            # 최대값은 가장 앞에다 저장
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(idx)

            # 윈도우 크기(k) 이상이면 맨 앞의 값을 제거
            if idx - window[0] >= k:
                window.popleft()

            # k- 1개 까지는 넣기만하고 그 후에 최대값을 리스트에 저장한다.
            if idx + 1 >= k:
                res.append(nums[window[0]])
        return res


"""
위에 있는 책의 풀이와 다른 점은 max 함수와 float('-inf'), window 에 숫자대신 인덱스를 넣는 것인데 
시간 복잡도의 영향을 주는 것은 max 함수이지 않을까 생각된다.
timeit 으로 속도를 측정할 때 해당 풀이가 책의 풀이보다 더 빨랐다.
단순히 max 함수이기 때문에 오래걸렸다기 보단 window 크기에서의 최대값이라는 제약이 있어 max 함수를 여러번 연산하기 때문에 타임아웃이 발생하지 않았을까 하는 생각이 든다. 
"""
