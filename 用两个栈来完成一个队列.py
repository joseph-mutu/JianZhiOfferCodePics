#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-13 15:55:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	a = []
	b = []
	def push(self,node):
		 self.a.append(node)
	def pop(self):
		if self.b:
			return self.b.pop()
		else:
			while self.a:
				self.b.append(self.a.pop())
			return self.b.pop()
s = Solution()
# PSH1","PSH2","PSH3","POP","POP","PSH4","POP","PSH5","POP","POP"]
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
# s.push(4)
# print(s.pop())
# s.push(5)
# print(s.pop())9
# print(s.pop())
