from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        state = []
        for char in tokens:
            if char == "+":
                state.append(state.pop() + state.pop())
            elif char == "-":
                second, first = state.pop(), state.pop()
                state.append(first - second)
            elif char == "*":
                state.append(state.pop() * state.pop())
            elif char == "/":
                second, first = state.pop(), state.pop()
                state.append(int(first / second))
            else:
                state.append(int(char))

        return state[0]


class SolutionMy:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(num2: int, num1: int, operation: str):
            if operation == '+':
                return num1 + num2
            elif operation == '-':
                return num1 - num2
            elif operation == '*':
                return num1 * num2
            elif operation == '/':
                if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
                    return abs(num1) // abs(num2)
                else:
                    return -(abs(num1) // abs(num2))

        state = []
        for token in tokens:
            if token.isnumeric():
                state.append(int(token))
            elif len(token) > 1 and token[0] == '-' and token[1:].isnumeric():
                state.append(-int(token[1:]))
            else:
                state.append(operation(state.pop(), state.pop(), token))

        return state[0]


if __name__ == '__main__':
    solution = Solution()

    tokens = ["2","1","+","3","*"]
    print(solution.evalRPN(tokens)) # 9

    tokens = ["4","13","5","/","+"]
    print(solution.evalRPN(tokens)) # 6

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(solution.evalRPN(tokens)) # 22
