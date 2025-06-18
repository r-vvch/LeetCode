from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])
        is_left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = [0] * level_size

            for i in range(level_size):
                node = queue.popleft()
                index = i if is_left_to_right else level_size - 1 - i
                current_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            is_left_to_right = not is_left_to_right

        return result


if __name__ == '__main__':
    solution = Solution()

    tn15 = TreeNode(15)
    tn7 = TreeNode(7)
    tn20 = TreeNode(20, tn15, tn7)
    tn9 = TreeNode(9)
    tn3 = TreeNode(tn9, tn20)
    print(solution.zigzagLevelOrder(tn3)) # [[3],[20,9],[15,7]]

    tn1 = TreeNode(1)
    print(solution.zigzagLevelOrder(tn1)) # [[1]]

    print(solution.zigzagLevelOrder([])) # []
