"""
[Medium] 687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/
"""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
문제의 힌트를 얻었다.
참고: https://leetcode.com/problems/longest-univalue-path/discuss/108142/Python-Simple-to-Understand
DFS 로 순회하여 각 Root 에서 같은 값의 가장 긴 경로를 리턴한다.
"""


class Solution:
    longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            longest_sum = 0
            if node.left and node.val == node.left.val:
                longest_sum += left_path + 1

            if node.right and node.val == node.right.val:
                longest_sum += right_path + 1

            self.longest = max(self.longest, longest_sum)
            return longest_sum

        dfs(root)
        return self.longest


"""
input 값이 [1,null,1,1,1,1,1,1] 인 경우 테스트에 실해했다.
이 풀이는 같은 값을 가진 모든 노드의 길이를 리턴한다.
이 문제는 가장 긴 "경로" 를 구하는 문제이므로 적절하지 않는 풀이이다.
"""


class Solution:
    longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            left_path = dfs(node.left)
            right_path = dfs(node.right)

            right_longest_sum = left_longest_sum = 0
            if node.left and node.val == node.left.val:
                left_longest_sum = left_path + 1

            if node.right and node.val == node.right.val:
                right_longest_sum = right_path + 1

            self.longest = max(self.longest, left_longest_sum + right_longest_sum)
            return max(left_longest_sum, right_longest_sum)

        dfs(root)
        return self.longest
