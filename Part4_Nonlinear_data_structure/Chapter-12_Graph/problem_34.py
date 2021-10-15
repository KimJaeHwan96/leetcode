"""
[medium] 46. Permutations
https://leetcode.com/problems/permutations/
"""
import copy
import itertools
from typing import List

"""
문제 해결은 다음과 같이 진행할 것이다.

1. nums 순회한다. 
2. 숫자를 하나 조회했으면 리스트에 넣고 그 값을 뺀 새로운 nums 를 만들어 재귀로 호출한다.
3. 순열을 만들었으면 결과값에 넣는다.

문제 34번인 https://leetcode.com/problems/letter-combinations-of-a-phone-number/ 과 같아 보여 비슷하게 풀어보았다. 
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(numbers, num_list):
            if len(nums) == len(num_list):
                result.append(num_list)
                return

            for idx, num in enumerate(numbers):
                copy_numbers = copy.copy(numbers)
                copy_numbers.pop(idx)
                # num_list.append(num)
                dfs(copy_numbers, num_list + [num])

        if not nums:
            return []

        result = []
        dfs(nums, [])
        return result


"""
num_list.append(num) 때문에 문제를 해결못했다.

언뜻 보면 리스트에 append 로 원소를 추가하는 것과 리스트 + [원소] 는 같아 보인다.

dfs(copy_numbers, num_list + [num]) 

vs 

num_list.append(num)
dfs(copy_numbers, num_list + [num])

이를 확인하기 위해 [1] + [2] 와 [1[.append(2) 의 주소값을 확인해보았다.
[1] + [2]의 주소값은 실행할 때마다 주소값이 계속달라지지만 [1[.append(2) 을 실행하면 주소값이 고정된다.
"""

"""
다른 사람의 코드를 확인해봤다.
출처: https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path):
            if not nums:
                res.append(path)

            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])

        res = []
        dfs(nums, [])
        return res


"""
아래의 책 풀이는 그전 문제에서 물피한 인자로 값을 저장하여 넘기는 방식으로 해결하지 않고 prev_elements 라는 하나의 공간을 이용하여 값을 저장했다.
dfs 함수가 재귀로 호출될때마다 prev_elements 에 값을 추가하고 그다음 순열을 찾기위해 dfs 호출 후 값을 제거하여 next_elements 의 각 값들로 순열을 생성한다.

차이점은 결국 prev_elements 에 저장하냐 인자에 값을 추가하여 저장하냐의 차이이다.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for element in elements:
                next_elements = elements[:]
                next_elements.remove(element)

                prev_elements.append(element)
                dfs(next_elements)
                prev_elements.remove(element)

        dfs(nums)
        return results


"""
itertools 모듈의 permutations 을 이용하면 쉽게 풀이된다.
참고: https://docs.python.org/ko/3/library/itertools.html#itertools.permutations
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
