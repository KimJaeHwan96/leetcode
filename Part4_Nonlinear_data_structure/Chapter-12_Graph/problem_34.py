"""
[medium] 46. Permutations
https://leetcode.com/problems/permutations/
"""
import copy
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
