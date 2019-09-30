#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 08:31:13
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		self.string_dict = {}
		self.first_appear = []
	def FirstAppearingOnce(self):
		if self.first_appear:
			return self.first_appear[0]
		else:
			return '#'
	def Insert(self, char):
		if self.string_dict.get(char):
			self.string_dict[char] += 1
			if char in self.first_appear:
				self.first_appear.pop(self.first_appear.index(char))
		else:
			self.string_dict[char] = 1
			self.first_appear.append(char)
# helloworld
s = Solution()
s.Insert('h')
print(s.FirstAppearingOnce())
s.Insert('e')
print(s.FirstAppearingOnce())
s.Insert('l')
print(s.FirstAppearingOnce())
s.Insert('l')
print(s.FirstAppearingOnce())
s.Insert('o')
print(s.FirstAppearingOnce())
s.Insert('w')
print(s.FirstAppearingOnce())
s.Insert('o')
print(s.FirstAppearingOnce())
s.Insert('r')
print(s.FirstAppearingOnce())
s.Insert('l')
print(s.FirstAppearingOnce())
s.Insert('d')
print(s.FirstAppearingOnce())
