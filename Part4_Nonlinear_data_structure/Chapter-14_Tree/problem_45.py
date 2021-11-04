"""
[Easy] 226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
"""
from typing import Optional


"""
DFS 로 루트노드의 왼쪽과 오른쪽 서브트리의 루트 노드를 바꿔주도록 하면 될 것 같다.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def dfs(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return root
