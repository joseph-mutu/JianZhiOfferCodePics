#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-21 16:01:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

# a = [[1],[2],[3]]
# a = [[1,2,3]]
# a = [[1,2],[3,4],[5,6],[7,8]]
# a = [[1,2,3],[4,5,6],[7,8,9]]
# a =  [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# a = [[1]]
# a = [[]]
a = [[1,2,3,4,5],[6,7,8,9,10]]
class Solution:
	def printMatrix(self, matrix):

		newList = []
		curLen = 0
		curCol = 0
		rightColEnd = len(matrix[0])
		downLenEnd = len(matrix)

		while downLenEnd > 0 and rightColEnd > 0:

			if rightColEnd > curCol and downLenEnd > curLen:
			# 打印第一行
				for j in range(curCol,rightColEnd):
					newList.append(matrix[curLen][j])

			#打印最后一列
			if downLenEnd > curLen + 1 and rightColEnd > curCol:
				for j in range(curLen+1,downLenEnd):
					newList.append(matrix[j][rightColEnd-1])
			#打印最后一行
			if rightColEnd - 2 > curCol-1 and rightColEnd-curCol >= 2 and downLenEnd-curLen >= 2:
				for i in range(rightColEnd-2,curCol-1,-1):
					newList.append(matrix[downLenEnd-1][i])

			# 打印第一列
			if downLenEnd - 2 > curLen and rightColEnd-curCol >= 2 and downLenEnd-curLen >= 3:
				for i in range(downLenEnd-2,curLen,-1):
					newList.append(matrix[i][curCol])


			curLen += 1
			curCol += 1

			rightColEnd -= 1
			downLenEnd -= 1
		return newList


s = Solution()
print(s.printMatrix(a))

