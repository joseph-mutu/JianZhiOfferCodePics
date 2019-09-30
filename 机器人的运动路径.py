#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-26 20:23:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:

	def digitSum(self,cur_row,cur_col,threshold):
		str_num_row = str(cur_row)
		str_num_col = str(cur_col)
		tem_sum = 0
		for dig in str_num_row:
			tem_sum += int(dig)
		for dig in str_num_col:
			tem_sum += int(dig)
		if tem_sum > threshold:
			return False
		return True
	def movingCount(self, threshold, rows, cols):
		if threshold < 0:
			return 0
		flag = [[0]*cols for i in range(rows)]
		self.BFS(0,0,rows,cols,flag,threshold)
		return sum(map(sum,flag))

	def BFS(self,cur_row,cur_col,rows,cols,flag,threshold):
		if cur_row < 0 or cur_row >= rows or cur_col < 0 or cur_col >= cols:
			return
		if flag[cur_row][cur_col] == 0 and self.digitSum(cur_row,cur_col,threshold):
			flag[cur_row][cur_col] = 1
			self.BFS(cur_row-1,cur_col,rows,cols,flag,threshold)
			self.BFS(cur_row,cur_col-1,rows,cols,flag,threshold)
			self.BFS(cur_row,cur_col+1,rows,cols,flag,threshold)
			self.BFS(cur_row+1,cur_col,rows,cols,flag,threshold)
		return 

s = Solution()
print(s.movingCount(10,1,100))

