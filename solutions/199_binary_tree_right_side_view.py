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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


class SolutionMy:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        branch = [root]
        left_history = set()
        right_history = set()
        while branch[-1]:
            if len(result) < len(branch):
                result.append(branch[-1].val)
            if branch[-1].right and branch[-1] not in right_history:
                right_history.add(branch[-1])
                branch.append(branch[-1].right)
            elif branch[-1].left and branch[-1] not in left_history:
                left_history.add(branch[-1])
                branch.append(branch[-1].left)
            else:
                if len(branch) > 1:
                    branch = branch[:-1]
                else:
                    break

        return result


if __name__ == '__main__':
    solution = Solution()

    tn5 = TreeNode(5)
    tn2 = TreeNode(2, None, tn5)
    tn4 = TreeNode(4)
    tn3 = TreeNode(3, None, tn4)
    tn1 = TreeNode(1, tn2, tn3)
    print(solution.rightSideView(tn1)) # [1,3,4]

    tn5 = TreeNode(5)
    tn4 = TreeNode(4, tn5, None)
    tn2 = TreeNode(2, tn4, None)
    tn3 = TreeNode(3)
    tn1 = TreeNode(1, tn2, tn3)
    print(solution.rightSideView(tn1)) # [1,3,4,5]

    tn3 = TreeNode(3)
    tn1 = TreeNode(1, None, tn3)
    print(solution.rightSideView(tn1)) # [1,3]

    print(solution.rightSideView(None)) # []

    #       4
    #      / \
    #     3   6
    #    /   /
    #   1   5
    #    \
    #     2
    tn2 = TreeNode(2)
    tn1 = TreeNode(1, None, tn2)
    tn3 = TreeNode(3, tn1, None)
    tn5 = TreeNode(5)
    tn6 = TreeNode(6, tn5, None)
    tn4 = TreeNode(4, tn3, tn6)
    print(solution.rightSideView(tn4)) # [4,6,5,2]
