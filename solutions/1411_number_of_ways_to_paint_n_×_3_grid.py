class Solution:
    def numOfWays(self, n: int) -> int:
        modulo = 1000000007
        x, y = 6, 6

        for i in range(2, n + 1):
            new_x = (3 * x + 2 * y) % modulo
            new_y = (2 * x + 2 * y) % modulo
            x, y = new_x, new_y

        return (x + y) % modulo


if __name__ == '__main__':
    solution = Solution()

    n = 1
    print(solution.numOfWays(n)) # 12

    n = 5000
    print(solution.numOfWays(n)) # 30228214
