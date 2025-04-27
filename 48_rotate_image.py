from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for depth in range(len(matrix) // 2):
            for i in range(len(matrix) - 1 - depth * 2):
                n = len(matrix) - 1 - depth
                temp_1 = matrix[i + depth][n]
                matrix[i + depth][n] = matrix[depth][i + depth]
                temp_2 = matrix[n][n - i]
                matrix[n][n - i] = temp_1
                temp_1 = matrix[n - i][depth]
                matrix[n - i][depth] = temp_2
                matrix[depth][i + depth] = temp_1


if __name__ == '__main__':
    solution = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix)
    print(matrix) # [[7,4,1],[8,5,2],[9,6,3]]
    assert(matrix) == [[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
    print(matrix) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    assert(matrix) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

    matrix = [[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35]]
    solution.rotate(matrix)
    # [11,12,13,14,15]     [31,26,21,16,11]
    # [16,17,18,19,20]     [32,27,22,17,12]
    # [21,22,23,24,25] ->  [33,28,23,18,13]
    # [26,27,28,29,30]     [34,29,24,19,14]
    # [31,32,33,34,35]     [35,30,25,20,15]
    print(matrix) # [[31,26,21,16,11],[32,27,22,17,12],[33,28,23,18,13],[34,29,24,19,14],[35,30,25,20,15]]
    assert(matrix) == [[31,26,21,16,11],[32,27,22,17,12],[33,28,23,18,13],[34,29,24,19,14],[35,30,25,20,15]]