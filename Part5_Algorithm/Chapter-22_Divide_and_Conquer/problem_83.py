"""
[Easy] 169. Majority Element
https://leetcode.com/problems/majority-element/
"""


"""
빈도 수를 구하는 문제이므로 Counter 가 먼저 생각났다.
문제는 한줄로 해결가능하지만 문할 정복으로 문제를 해결하는 방법에 대한 고민이 필요하다. 
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


"""
병합정렬로 문제를 푼다는 생각을 하지 못했는데 책의 풀이과정을 보고 알았다.
분할 한 후 정복하는 코드에서 이렇게도 풀수있다는 것을 알았다. 
하지만 input 으로 [1,2,1,3,1,4,1,5] 를 넣으니 5 가 나왔다. 그러므로 정렬을 한 후 알고리즘을 사용해야한다고 생각되었다.
"""


class Solution:
    def majorityElement(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > half]

"""
풀이를 보다가 처음보는 알고리즘을 보았다. 보이어-무어 과반수 투표 알고리즘(Boyer-Moore Voting Algorithm)
코드를 보니 간단하면서 직관적인 알고리즘이다. 
하지만 병합정렬과 같이 정렬을 해주어야 할것같다.
input 으로 [1,2,1,3,1,4,5,1] 를 넣으니 5 가 나왔다. 풀이과정의 오류인듯 보인다.(혹은 잘못 이해한 것일 수도 있음)
그러므로 정렬을 한 후 알고리즘을 사용해야한다고 생각되었다.
"""


class Solution:
    def majorityElement(self, nums):
        nums.sort() # 정렬 추가
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
