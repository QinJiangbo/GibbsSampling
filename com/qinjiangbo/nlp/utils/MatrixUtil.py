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


if "__main__" == __name__:
    MatrixUtil.get_array()
