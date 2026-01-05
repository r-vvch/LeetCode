from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        negative_count = 0
        min_abs_value = float('inf')

        for row in matrix:
            for value in row:
                total_sum += abs(value)
                if value < 0:
                    negative_count += 1
                min_abs_value = min(min_abs_value, abs(value))

        if negative_count % 2 == 1:
            total_sum -= 2 * min_abs_value

        return total_sum



if __name__ == '__main__':
    solution = Solution()

    matrix = [[1,-1],[-1,1]]
    print(solution.maxMatrixSum(matrix)) # 4

    matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
    print(solution.maxMatrixSum(matrix)) # 16
