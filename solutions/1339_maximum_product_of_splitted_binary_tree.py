from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(' + str(self.val) + ')'


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        node_sums = []
        max_sum = 0

        def dfs(node):
            if not node:
                return 0
            curr_sum = node.val + dfs(node.left) + dfs(node.right)
            node_sums.append(curr_sum)
            return curr_sum

        total = dfs(root)

        for x in node_sums:
            max_sum = max(max_sum, (total - x)*x)

        return max_sum % (10**9 + 7)


if __name__ == '__main__':
    solution = Solution()

    tn4 = TreeNode(4)
    tn5 = TreeNode(5)
    tn2 = TreeNode(2, tn4, tn5)
    tn6 = TreeNode(6)
    tn3 = TreeNode(3, tn6)
    tn1 = TreeNode(1, tn2, tn3)
    print(solution.maxProduct(tn1))

    tn5 = TreeNode(5)
    tn6 = TreeNode(6)
    tn4 = TreeNode(4, tn5, tn6)
    tn3 = TreeNode(3)
    tn2 = TreeNode(2, tn3, tn4)
    tn1 = TreeNode(1, None, tn2)
    print(solution.maxProduct(tn1))
