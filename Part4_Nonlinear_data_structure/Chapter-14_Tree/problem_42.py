"""
[Easy] 104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        queue = deque([root])
        if not root:
            return 0

        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


"""
if node.left:  &  if node.right: 
분기문을 추가한 이유?
-> left 와 right 가 None 인경우 포함을 시키면 안됨.  
    해당 분기가 없으면 None 도 큐에 포함하여 원래 depth 보다 1 큼
    
for node in queue 이 아닌 for _ in range(len(queue)) 를 사용한 이유?
-> iteration 시 queue 에 값을 추가하여 문제가 생긴다. 설령 문제가 생기지 않더라도 각 depth 의 노드들만 순회해야하므로 현재 큐에 있는 노드들만 조회해야 한다.
"""


"""
DFS 풀이
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return max(left_height, right_height) + 1

        depth = dfs(root)
        return depth + 1


"""
BFS 보다 DFS 가 더 간결하게 풀이 가능해보여 시도해보았다.
사실 DFS 는 height 를 구하는 풀이 방법이고 이 문제는 depth 를 구하는 문제이기 때문에 BFS 를 사용하는 것 맞다.
다만 해결방법은 비슷하니 풀이해보았다.
"""
