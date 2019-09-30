#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-26 06:14:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		self.is_path = False
	def hasPath(self, matrix, rows, cols, path):
		if not matrix or rows <= 0 or cols <= 0 or not path:
			return False
		flag = [[0]*cols for i in range(rows)]
		cur_pos = 0
		for i in range(rows):
			for j in range(cols):
				if self.is_path:
					break
				if flag[i][j] != 1:
					self.SearchPathDFS(i,j,cur_pos,matrix,rows,cols,path,flag)

		return self.is_path
	def SearchPathDFS(self,cur_row,cur_col,cur_pos,matrix,rows,cols,path,flag):
		if cur_pos >= len(path):
			self.is_path = True
			return 
		if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
			return
		if not self.is_path and flag[cur_row][cur_col] == 0 and matrix[cur_row*cols + cur_col] == path[cur_pos]:
			
			flag[cur_row][cur_col] = 1
			self.SearchPathDFS(cur_row,cur_col-1,cur_pos+1,matrix,rows,cols,path,flag)
			self.SearchPathDFS(cur_row-1,cur_col,cur_pos+1,matrix,rows,cols,path,flag)
			self.SearchPathDFS(cur_row,cur_col+1,cur_pos+1,matrix,rows,cols,path,flag)
			self.SearchPathDFS(cur_row+1,cur_col,cur_pos+1,matrix,rows,cols,path,flag)
			flag[cur_row][cur_col] = 0
		return
# matrix = "abcesfcsadee"
matrix = 'ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS'
path = 'SGGFIECVAASABCEHJIGQEM'
s = Solution()
print(s.hasPath(matrix,5,8,path))
