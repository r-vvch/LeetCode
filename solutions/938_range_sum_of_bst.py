from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        summ = 0
        if low <= root.val <= high:
            summ += root.val
            summ += self.rangeSumBST(root.left, low, high)
            summ += self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            summ += self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            summ += self.rangeSumBST(root.left, low, high)

        return summ

    def rangeSumBSTnaive(self, root: Optional[TreeNode], low: int, high: int) -> int:
        summ = 0
        if low <= root.val <= high:
            summ += root.val
        if root.left:
            summ += self.rangeSumBST(root.left, low, high)
        if root.right:
            summ += self.rangeSumBST(root.right, low, high)
        return summ


if __name__ == '__main__':
    solution = Solution()

    tn_3 = TreeNode(3, None, None)
    tn_7 = TreeNode(7, None, None)
    tn_5 = TreeNode(5, tn_3, tn_7)
    tn_18 = TreeNode(18, None, None)
    tn_15 = TreeNode(15, None, tn_18)
    tn_10 = TreeNode(10, tn_5, tn_15)
    low = 7
    high = 15
    print(solution.rangeSumBST(tn_10, low, high)) # 32

    root = [10,5,15,3,7,13,18,1,None,6]
    tn_1 = TreeNode(1, None, None)
    tn_3 = TreeNode(1, tn_1, None)
    tn_6 = TreeNode(6, None, None)
    tn_7 = TreeNode(7, tn_6, None)
    tn_5 = TreeNode(5, tn_3, tn_7)
    tn_13 = TreeNode(13, None, None)
    tn_18 = TreeNode(18, None, None)
    tn_15 = TreeNode(15, tn_13, tn_18)
    tn_10 = TreeNode(10, tn_5, tn_15)
    low = 6
    high = 10
    print(solution.rangeSumBST(tn_10, low, high)) # 23
