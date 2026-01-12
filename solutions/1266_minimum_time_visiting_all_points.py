from itertools import pairwise
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum_steps = 0
        for i in range(1, len(points)):
            sum_steps += max(abs(points[i][0] - points[i - 1][0]),
                             abs(points[i][1] - points[i - 1][1]))
        return sum_steps

class SolutionOneLiner:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(P[0] - Q[0]), abs(P[1] - Q[1])) for P, Q in pairwise(points))


if __name__ == '__main__':
    solution = Solution()

    points = [[1,1],[3,4],[-1,0]]
    print(solution.minTimeToVisitAllPoints(points)) # 7

    points = [[3,2],[-2,2]]
    print(solution.minTimeToVisitAllPoints(points)) # 5
