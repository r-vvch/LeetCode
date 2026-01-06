from typing import Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(' + str(self.val) + ')'


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_lvl = 1
        max_sum = float('-inf')
        ans = 1

        queue = deque([root])

        while queue:
            curr_sum = 0
            lvl_size = len(queue)

            for _ in range(lvl_size):
                node = queue.popleft()
                curr_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                ans = curr_lvl

            curr_lvl += 1

        return ans


class SolutionMy:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels_sum = defaultdict(int)

        def dfs(node, depth):
            if not node:
                return
            levels_sum[depth] += node.val
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 1)

        max_sum = {'level': 1, 'val': levels_sum[1]}
        for level in levels_sum:
            if levels_sum[level] > max_sum['val']:
                max_sum['level'] = level
                max_sum['val'] = levels_sum[level]

        return max_sum['level']


if __name__ == '__main__':
    solution = Solution()

    tn_7_low = TreeNode(7)
    tn_minus_8 = TreeNode(-8)
    tn_7_high = TreeNode(7, tn_7_low, tn_minus_8)
    tn_0 = TreeNode(0)
    tn_1 = TreeNode(1, tn_7_high, tn_0)
    print(solution.maxLevelSum(tn_1)) # 2
