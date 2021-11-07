"""
[Easy] 110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
from typing import Optional


"""
간단한 문제로 각 서브트리의 depth 의 차가 1 이하이면 balanced 이므로 True 아니면 False 를 리턴하면된다. 
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    height_diff = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.depth_diff = max(self.depth_diff, abs(left_height - right_height))
            return max(left_height, right_height) + 1

        dfs(root)
        if self.height_diff > 1:
            return False
        return True


"""
문제를 푼 후 비효율적인 부분을 발견했다. 서브트리에서 balanced 가 아닌 경우 더이상 연산을 할 필요없이 False 만 리턴하면 된다.
이를 이용해 최적화를 해보았다.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1

        return dfs(root) >= 0
