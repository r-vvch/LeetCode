from math import inf
from typing import List


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        min_x, max_x = inf, -inf
        point_set = set()
        for x, y in points:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            point_set.add((x, y))

        s = min_x + max_x
        # sym_line_x = s / 2

        for x, y in points:
            # x "brother" should be at x - 2*(x - sym_line_x) or x + 2*(sym_line_x - x)
            # x - 2*(x - sym_line_x) = x - 2*x + 2*sym_line_x = 2*sym_line_x - x = s - x
            # x + 2*(sym_line_x - x) = x + 2*sym_line_x - 2*x = 2*sym_line_x - x = s - x
            # so we get:
            if (s - x, y) not in point_set:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()

    points = [[1,1],[-1,1]]
    print(solution.isReflected(points))
    # True
    assert solution.isReflected(points) == True
    # Explanation: We can choose the line x = 0.

    points = [[1,1],[-1,-1]]
    print(solution.isReflected(points))
    # False
    assert solution.isReflected(points) == False
    # Explanation: We can't choose a line.
