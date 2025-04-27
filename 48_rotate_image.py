from typing import List
import numpy as np
import time

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

    matrix_1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix_2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    matrix_3 = [[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30],[31,32,33,34,35]]

    start_time = time.time()

    print(np.rot90(matrix_1, axes=(1,0)).tolist())
    print(np.rot90(matrix_2, axes=(1,0)).tolist())
    print(np.rot90(matrix_3, axes=(1,0)).tolist())

    print("NumPy time: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()

    solution.rotate(matrix_1)
    print(matrix_1) # [[7,4,1],[8,5,2],[9,6,3]]
    solution.rotate(matrix_2)
    print(matrix_2) # [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    solution.rotate(matrix_3)
    print(matrix_3) # [[31,26,21,16,11],[32,27,22,17,12],[33,28,23,18,13],[34,29,24,19,14],[35,30,25,20,15]]

    print("My time: --- %s seconds ---" % (time.time() - start_time))

    assert(matrix_1) == [[7,4,1],[8,5,2],[9,6,3]]
    assert(matrix_2) == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    assert(matrix_3) == [[31,26,21,16,11],[32,27,22,17,12],[33,28,23,18,13],[34,29,24,19,14],[35,30,25,20,15]]

    # [11,12,13,14,15]     [31,26,21,16,11]
    # [16,17,18,19,20]     [32,27,22,17,12]
    # [21,22,23,24,25] ->  [33,28,23,18,13]
    # [26,27,28,29,30]     [34,29,24,19,14]
    # [31,32,33,34,35]     [35,30,25,20,15]
