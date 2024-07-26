from typing import List

# 73. Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.
# Input: matrix =
# [[1, 1, 1],
#  [1, 0, 1],
#  [1, 1, 1]]

# Output:
# [[1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i_lst = []
        j_lst = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in i_lst:
                        i_lst.append(i)
                    if j not in j_lst:
                        j_lst.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in i_lst or j in j_lst:
                    matrix[i][j] = 0

        print(matrix)


Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
