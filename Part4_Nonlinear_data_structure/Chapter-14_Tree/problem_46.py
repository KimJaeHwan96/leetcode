"""
[Easy] 617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
"""


from typing import Optional


"""
두 개의 루트 노드들이 주어지는데 첫 번째 루트노드의 트리에 병합하도록 풀이하면 될 것같다.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2):
            return root1 or root2

        left_node = self.mergeTrees(root1.left, root2.left)
        right_node = self.mergeTrees(root1.right, root2.right)

        if not root1.left:
            root1.left = left_node

        if not root1.right:
            root1.right = right_node

        root1.val += root2.val
        return root1


"""
좀더 가독성이 좋게 풀이하려면 새로운 노드에 연결하는 형태도 좋아보인다.
"""


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not (root1 and root2):
            return root1 or root2

        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node


"""
아예 새로운 노드를 생성하여 새로운 트리를 만든다.
공간 복잡도에 좋지는 않겠지만 가독성은 훨씬 좋아보인다.
"""
