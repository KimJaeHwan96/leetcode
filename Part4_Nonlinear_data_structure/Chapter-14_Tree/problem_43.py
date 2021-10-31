"""
[Easy] 543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""
from typing import Optional

"""
루트 노드를 기준으로 왼쪽 서브트리의 depth 와 오른쪽 서브트리의 depth 의 합이다.
DFS 의 재귀로 풀이 가능해보인다.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        잘못된 로직
        """
        def dfs(node):
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            return left_depth + right_depth

        return dfs(root)


"""
왼쪽 서브트리의 depth 와 오른쪽 서브트리의 depth 의 합 을 구하기 위해 리프 노드에 도착하면 어떤 값을 리턴할 것인지 고민을 많이 했다.
0 을 리턴하면 +1 또는 +2 를 해야하는데 [1] 을 입력값을 주면 0이 아닌 1 또는 3이 되니 안된다.
그렇다고 1 을 리턴해도 문제가 생긴다.
"""


class Solution:
    diameter_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            self.diameter_length = max(self.diameter_length, left_height + right_height + 2)
            return max(left_height, right_height) + 1

        dfs(root)
        return self.diameter_length


"""
** 용어를 잘못 사용했는데 depth 는 내려갈 수록 값이 커지는데 해당 로직은 올라갈 수록 값이 커지니 depth 가 아닌 height 가 맞는 용어이다. **

그렇다면 경로의 길이와 각 노드의 height 를 따로 구하면 어떨까?

경로의 길이 = 왼쪽 서브트리의 height 와 오른쪽 서브트리의 height 의 합 + 2
Root 노드의 height = 왼쪽 서브트리의 height 와 오른쪽 서브트리의 height 중 가장 큰 값 + 1

리프 노드의 존재하지 않은 노드들에 대해서는 -1을 리턴하는데 0을 리턴하지 않고 왜 -1 을 리턴할까?
-> 경로의 길이는 간선의 합이기 때문에 각 서브 트리의 height 의 합에 +2를 한다. 그리고 리프노드의 height 는 0 이니 존재하지 않는 노드는 -1 이 되어야 맞을 것같다.
참고: https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python/591034
"""
