# coding=utf-8

"""
   Date: 18/11/2016
   Author: qinjiangbo@github.io
   Description:
   Matrix tools for processing complex matrix computation
"""


class MatrixUtil(object):
    @classmethod
    def get_array(cls):
        nums = [[1, 2, 3], [4, 5], [2]]
        for i in range(3):
            for j in range(len(nums[i])):
                print(nums[i][j], end=" ")
            print()
        return nums

    @classmethod
    def print_1D_array(cls, one_dim_array):
        for i in range(len(one_dim_array)):
            print(one_dim_array[i], end=" ")

    @classmethod
    def print_2D_array(cls, two_dim_array):
        for i in range(len(two_dim_array)):
            for j in range(len(two_dim_array[i])):
                print(two_dim_array[i][j], end=" ")
            print()

if "__main__" == __name__:
    one_dimension = [1, 4, 6, 3, 8, 6, 8, 4.5, 9.0]
    MatrixUtil.print_1D_array(one_dimension)
    two_dimension = [[1, 5, 6], [3, 5, 8], [13, 72, 90], [23, 45]]
    MatrixUtil.print_2D_array(two_dimension)
