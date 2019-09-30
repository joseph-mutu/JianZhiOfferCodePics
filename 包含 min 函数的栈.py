#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-22 11:59:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	minList = []
	data = []
	curMin = 99999999
	def push(self,node):
		self.data.append(node)
		if self.curMin > node:
			self.minList.append(node)
			self.curMin = node
	def pop(self):
		if self.data:
			tem = self.data[-1]
			if tem == self.curMin and self.minList:
				del self.minList[-1]
			del self.data[-1]
			return tem
		else:
			return None
	def top(self):
		if data:
			return self.data[-1]
		else:
			return None

	def min(self):
		if self.minList:
			return self.minList[-1]
		else:
			return None

s = Solution()
s.push(3)
print(s.min())
s.push(4)
print(s.min())
s.push(2)
print(s.min())
s.push(3)
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())
s.pop()
print(s.min())