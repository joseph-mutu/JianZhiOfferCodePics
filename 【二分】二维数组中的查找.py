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
		find = False
		find_pos = -1
		for i in range(len(data)):
			cur_row = data[i]
			if len(cur_row) == 0:
				break
			elif cur_row[0] > want_num:
				break
			else:
				start = 0
				end = len(cur_row) - 1
				while end - start >= 0:
					search_pos = int((start+end)/2)
					if cur_row[search_pos] < want_num: 
						start = search_pos + 1
					elif cur_row[search_pos] > want_num:
						end = search_pos - 1
					elif cur_row[search_pos] == want_num:
						find = True
						find_pos = search_pos
						break
				if find:
					break
				else:
					continue
		if not find:
			return False
		else:
			return True



# num_raw = 3
# data = np.full((3,5),0,dtype = int)
# want_num = 17

# for i in range(num_raw):
# 	data[i] = list(map(int,input().split()))
want_num = 16
data = [[]]
S = Solution()
S.Find(want_num,data)