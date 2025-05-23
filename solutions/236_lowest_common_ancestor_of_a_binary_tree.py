class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right


if __name__ == '__main__':
    solution = Solution()

    tn_7 = TreeNode(7, None, None)
    tn_4 = TreeNode(4, None, None)
    tn_2 = TreeNode(2, tn_7, tn_4)
    tn_6 = TreeNode(6, None, None)
    tn_5 = TreeNode(5, tn_6, tn_2)
    tn_0 = TreeNode(0, None, None)
    tn_8 = TreeNode(8, None, None)
    tn_1 = TreeNode(1, tn_0, tn_8)
    tn_3 = TreeNode(3, tn_5, tn_1)
    root = tn_3

    p = tn_5
    q = tn_1
    print(solution.lowestCommonAncestor(root, p, q)) # 3

    p = tn_5
    q = tn_4
    print(solution.lowestCommonAncestor(root, p, q)) # 5

    tn_1 = TreeNode(1, tn_2, None)
    tn_2 = TreeNode(2, None, None)
    root = tn_1

    p = tn_1
    q = tn_2
    print(solution.lowestCommonAncestor(root, p, q)) # 1
