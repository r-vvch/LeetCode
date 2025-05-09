from random import randint

# The rand7() API is already defined for you.
def rand7():
    # @return a random integer in the range 1 to 7
    return randint(1, 7)

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        result = 40
        while result >= 40:
            result = 7 * (rand7() - 1) + (rand7() - 1)
        return result % 10 + 1

    def rand10_another(self):
        i = 7
        while i > 6:        # when loop ends, i can be 1,2,3,4,5,6
            i = rand7()
        j = 6
        while j > 5:        # when loop ends, j can be 1,2,3,4,5
            j = rand7()
        if i % 2 == 0:
            return j
        else:
            return j+5


if __name__ == '__main__':
    solution = Solution()

    n = 1
    for i in range(n):
        print(solution.rand10())
    print()

    n = 2
    for i in range(n):
        print(solution.rand10())
    print()

    n = 3
    for i in range(n):
        print(solution.rand10())
    print()
