from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs(left, right, p_str):
            # left is a number of open parentesis, right -- closed
            # p_str is a parentesis string we will be adding to result

            if len(p_str) == n * 2:
                output.append(p_str)
                return

            if left < n:
                dfs(left + 1, right, p_str + '(')

            if right < left:
                dfs(left, right + 1, p_str + ')')

        dfs(0, 0, '')
        return output

    def generateParenthesisIter(self, n: int) -> List[str]:
        # slower then recursion
        output = []
        left = right = 0

        status = [(left, right, '')]
        while status:
            left, right, s = status.pop()
            if len(s) == 2 * n:
                output.append(s)
            if left < n:
                status.append((left + 1, right, s + '('))
            if right < left:
                status.append((left, right + 1, s + ')'))

        return output


if __name__ == '__main__':
    solution = Solution()

    print(solution.generateParenthesis(3))
    assert solution.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]

    print(solution.generateParenthesis(1))
    assert solution.generateParenthesis(1) == ["()"]
