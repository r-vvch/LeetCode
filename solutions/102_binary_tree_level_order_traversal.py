from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = [0] * level_size

            for i in range(level_size):
                node = queue.popleft()
                current_level[i] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


if __name__ == '__main__':
    solution = Solution()

    tn15 = TreeNode(15)
    tn7 = TreeNode(7)
    tn20 = TreeNode(20, tn15, tn7)
    tn9 = TreeNode(9)
    tn3 = TreeNode(3, tn9, tn20)
    print(solution.levelOrder(tn3)) # [[3],[9,20],[15,7]]

    tn1 = TreeNode(1)
    print(solution.levelOrder(tn1)) # [[1]]

    print(solution.levelOrder([])) # []
