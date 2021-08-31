"""
[Easy] 53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
import sys
from typing import List

"""
이중 반복문으로 각 서브배열들의 합을 더해가면서 더 큰 값을 찾도록 구현했다.
하지만 타임아웃이 나와 시간복잡도 O(n^2) 으로는 해결할 수 없었다.   
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = -sys.maxsize
        first_pointer = 0
        while first_pointer < len(nums):
            sub_result = 0
            for num in nums[first_pointer:]:
                sub_result += num
                result = max(result, sub_result)
                if result < 0:
                    break
            first_pointer += 1
        return result


"""
이 문제를 어떻게 메모이제이션으로 풀 수 있을지 고민을 했다. 
가장 큰 값을 저장하는 방향으로만 생각했는데 책에서는 앞에서부터 누적 합을 구하는 방향으로 메모이제이션 풀이 방법을 제시했다.
곰곰히 생각해보니 앞의 숫자가 0 보다 큰 값을 더해나가면 각 값들은 서브 배열의 값이 된다. 
결국 계산을 다 하면 각 값들은 서브배열들을 "기억"하게 된다. 이런 풀이방법도 있구나 하는 감탄이 있었다.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)


"""
연속되어 있다는 제약사항과 메모이제이션을 이용하는 풀이방법인 것 같다.
그다음 풀이방법으로 카데인 알고리즘으로 이용한 풀이가 있는데 카데인 알고리즘에 대해서 공부를 했다.
"""


"""
이 문제는 1977년 제안된 매우 유명한 컴퓨터 과학 알고리즘 문제이고 제이 카데인이 O(n)에 풀이가 가능하도록 고안한 카데인 알고리즘을 만들었다.
최대 서브 배열을 찾기 위해 어디서 시작되는지를 찾는 문제 O(n^2) 풀이에서 각 단계마다 최대값을 담어 어디서 끝나는지 찾는 문제 O(n) 풀이로 치환해서 풀었다.

해당 내용은 메모이제이션으로 풀이한 방향과 느낌이 유사하다. 0 보다 큰 경우만 더해가면 각 배열의 값들은 어디서 시작되는지가 아닌 어디서 끝나는지에 대한 최대 합이 된다.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum


"""
각 단계의 최대값을 구하면서 그 중 최대값을 구한다. 메모이제이션 풀이방법과 실행시간은 동일하다
"""
