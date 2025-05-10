from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def valid(self, root, minimum, maximum):
            if not root:
                return True
            if not (minimum < root.val < maximum):
                return False
            return (self.valid(root.left, minimum, root.val) and
                    self.valid(root.right, root.val, maximum))

    def isValidBSTFast(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))


    def findMin(self, root: Optional[TreeNode]) -> bool:
        while root.left:
            return self.findMin(root.left)
        return root.val

    def findMax(self, root: Optional[TreeNode]) -> bool:
        while root.right:
            return self.findMax(root.right)
        return root.val

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        elif (not root.left and root.right
              and root.val < root.right.val and root.val < self.findMin(root.right)):
            return self.isValidBST(root.right)
        elif (root.left and not root.right
              and root.left.val < root.val and self.findMax(root.left) < root.val):
            return self.isValidBST(root.left)
        elif (root.left and root.right
              and root.left.val < root.val < root.right.val
              and self.findMax(root.left) < root.val < self.findMin(root.right)):
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False


if __name__ == '__main__':
    solution = Solution()

    tn_1 = TreeNode(1, None, None)
    tn_3 = TreeNode(3, None, None)
    tn_2 = TreeNode(2, tn_1, tn_3)
    print(solution.isValidBST(tn_2)) # True

    tn_1 = TreeNode(1, None, None)
    tn_3 = TreeNode(3, None, None)
    tn_6 = TreeNode(6, None, None)
    tn_4 = TreeNode(4, tn_3, tn_6)
    tn_5 = TreeNode(5, tn_1, tn_4)
    print(solution.isValidBST(tn_5)) # False

    tn_11 = TreeNode(1, None, None)
    tn_1 = TreeNode(1, None, tn_11)
    print(solution.isValidBST(tn_5)) # False

    tn_7 = TreeNode(7, None, None)
    tn_3 = TreeNode(3, None, None)
    tn_6 = TreeNode(6, tn_3, tn_7)
    tn_4 = TreeNode(4, None, None)
    tn_5 = TreeNode(5, tn_4, tn_6)
    print(solution.isValidBST(tn_5)) # False

    tn_m1 = TreeNode(-1, None, None)
    tn_0 = TreeNode(0, tn_m1, None)
    print(solution.isValidBST(tn_0)) # True
