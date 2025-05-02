class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack) == 0:
                stack.append(i)
            else:
                if (stack[-1] == '(' and i == ')' or stack[-1] == '[' and i == ']'
                    or stack[-1] == '{' and i == '}'):
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()

    s = "()"
    print(solution.isValid(s)) # True
    # assert solution.isValid(s) == True

    s = "()[]{}"
    print(solution.isValid(s)) # True
    # assert solution.isValid(s) == True

    s = "(]"
    print(solution.isValid(s)) # False
    # assert solution.isValid(s) == False

    s = "([])"
    print(solution.isValid(s)) # True
    # assert solution.isValid(s) == True
