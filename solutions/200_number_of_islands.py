from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if (0 <= r < rows and 0 <= c < cols and
                        grid[r][c] == "1" and (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands


if __name__ == '__main__':
    solution = Solution()

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(solution.numIslands(grid)) # 1

    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(solution.numIslands(grid)) # 3
