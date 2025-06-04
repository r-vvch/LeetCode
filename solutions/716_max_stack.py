class MaxStack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        output = '['
        for i in self.stack:
            output += str(i) + ', '
        output = output[:-2]
        output += ']'
        return output

    def push(self, x: int):
        # Pushes element x onto the stack.
        self.stack.append(x)

    def pop(self):
        # Removes the element on top of the stack and returns it.
        return self.stack.pop()

    def top(self):
        # Gets the element on the top of the stack without removing it.
        return self.stack[-1]

    def peekMax(self):
        # Retrieves the maximum element in the stack without removing it.
        return max(i for i in self.stack)

    def popMax(self):
        # Retrieves the maximum element in the stack and removes it.
        # If there is more than one maximum element, only remove the top-most one.
        stack_max_i = 0
        for i in range(len(self.stack)):
            if self.stack[i] >= self.stack[stack_max_i]:
                stack_max_i = i
        return self.stack.pop(stack_max_i)


if __name__ == '__main__':
    stk = MaxStack()

    stk.push(5)
    print(stk)            # [5] the top of the stack and the maximum number is 5.
    stk.push(1)
    print(stk)            # [5, 1] the top of the stack is 1, but the maximum is 5.
    stk.push(5)
    print(stk)            # [5, 1, 5] the top of the stack is 5, which is also the maximum,
                          #           because it is the top most one.

    print(stk.top())      # return 5, [5, 1, 5] the stack did not change.
    print(stk.popMax())   # return 5, [5, 1] the stack is changed now,
                          #                  and the top is different from the max.
    print(stk.top())      # return 1, [5, 1] the stack did not change.
    print(stk.peekMax())  # return 5, [5, 1] the stack did not change.
    print(stk.pop())      # return 1, [5] the top of the stack and the max element is now 5.
    print(stk.top())      # return 5, [5] the stack did not change.
