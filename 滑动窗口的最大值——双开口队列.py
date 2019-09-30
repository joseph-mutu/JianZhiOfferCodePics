#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-24 20:06:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:

	def __init__(self):
		self.index = []
		self.max = []
	def maxInWindows(self, num, size):
		if not num or size <= 0 or size >= len(num):
			return []

		for i in range(0,size):
			while self.index and num[self.index[-1]] <= num[i]:
				self.index.pop()
			self.index.append(i)

		for i in range(size,len(num)):
			self.max.append(num[self.index[0]])
			while self.index and num[self.index[-1]] <= num[i]:
				self.index.pop()
			if self.index and self.index[0] <= (i - size):
				self.index.pop(0)
			self.index.append(i)
		self.max.append(num[self.index[0]])
		return self.max

s = Solution()
print(s.maxInWindows([2,3,4,2,6,2,5,1],3))
