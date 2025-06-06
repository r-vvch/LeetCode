from math import sqrt


class SolutionMath:
    def isSquare(self, n: int) -> bool:
        if int(sqrt(n))**2 == n:
            return True

    # Based on Lagrange's Four Square theorem, there are only 4 possible results: 1, 2, 3, 4.
    def numSquares(self, n: int) -> int:
        # How to check if number is full square?
        # Just compare square of integer part of root and this number. O(1).    
        if self.isSquare(n):
            return 1

        # How to check if number is sum of 2 squares: n = i*i + j*j?
        # Iterate over all i < sqrt(n) and check that n - i*i is full square. O(sqrt(n)).
        sqrt_n = int(sqrt(n))
        for i in range(1, sqrt_n + 1):
            if self.isSquare(n - i*i):
                return 2

        # How to check that number is sum of 4 squares?
        # Based on Legendre's three-square theorem,
        # the result is 3 if and only if n can NOT be written in the form of 4^a * (8 * b + 7).
        # So, if that statement is true -- the only possible solution if 4 sqares.
        n_temp = n
        while n_temp % 4 == 0:
            n_temp /= 4
        if n_temp % 8 == 7:
            return 4
        
        return 3


class SolutionDinProg:
    def numSquares(self, n: int) -> int:
        # num_sqares[i] is a minimal num of perfect sqares that sum to i
        num_sqares = [float('inf')] * (n + 1)
        num_sqares[0] = 0

        for num in range(1, n + 1):
            i = 1
            while i * i <= num:
                num_sqares[num] = min(num_sqares[num], num_sqares[num - i * i] + 1)
                i += 1

        return num_sqares[n]


Solution = SolutionMath
# Solution = SolutionDinProg


if __name__ == '__main__':
    solution = Solution()

    n = 12
    print(solution.numSquares(n)) # 3

    n = 13
    print(solution.numSquares(n)) # 2
