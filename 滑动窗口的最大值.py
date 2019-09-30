#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-23 18:31:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:

	def __init__(self):
		self.max = []
	def maxInWindows(self, num, size):
		if not num or size <= 0 or size > len(num):
			return []
		start = 0
		end = size
		while end < len(num)+1:
			tem_max = -99
			for i in range(start,end):
				if num[i] > tem_max:
					tem_max = num[i]
			self.max.append(tem_max)
			start += 1
			end += 1
		return self.max

s = Solution()
num = [2,3,4,2,6,2,5,1]
print(s.maxInWindows(num,12))



