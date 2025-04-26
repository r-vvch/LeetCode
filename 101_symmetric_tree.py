from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val
                and self.isMirror(left.left, right.right)
                and self.isMirror(left.right, right.left))
    
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)


if __name__ == '__main__':
    solution = Solution()

    tn_7 = TreeNode(3, None, None)
    tn_6 = TreeNode(4, None, None)
    tn_5 = TreeNode(2, tn_7, tn_6)
    tn_4 = TreeNode(4, None, None)
    tn_3 = TreeNode(3, None, None)
    tn_2 = TreeNode(2, tn_4, tn_3)
    tn_1 = TreeNode(1, tn_5, tn_2)

    print(solution.isSymmetric(tn_1))

    tn_5 = TreeNode(3, None, None)
    tn_4 = TreeNode(2, None, tn_5)
    tn_3 = TreeNode(3, None, None)
    tn_2 = TreeNode(2, None, tn_3)
    tn_1 = TreeNode(1, tn_4, tn_2)
    
    print(solution.isSymmetric(tn_1))
