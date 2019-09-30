#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-06 18:33:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

# class search_2D_matirx:

# 	def search(self,num):
import os
import numpy as np

class Solution:
	def Find(self,want_num,data):
		find  =False
		# 从左下角开始查找，如果want_num 比当前的值大，向右移动
		# 比当前的值小，向上移动
		num_raw = len(data)
		num_col = len(data[0])
		if num_col == 0:
			return False
		else:
			raw = num_raw -1 
			col = 0
			while raw >= 0 and col < num_col:
				if data[raw][col] < want_num:
					col += 1
				elif data[raw][col] > want_num:
					raw -= 1
				elif data[raw][col] == want_num:
					find = True
					break
		if find:
			return True
		else:
			return False




want_num = 15
data = [[1,2,3,4,5],[5,6,7,8,9],[10,11,12,13,14]]
S = Solution()
S.Find(want_num,data)