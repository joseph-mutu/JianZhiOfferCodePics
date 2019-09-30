#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-01 17:49:39
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

import functools as f
class Solution:
	def PrintMinNumber(self, numbers):
		if numbers:
			str_numbers = [str(num) for num in numbers]
			str_numbers = sorted(str_numbers,key = f.cmp_to_key(self.Compare))
			return "".join(str_numbers)
		else:
			return ""

	def Compare(self,s1,s2):
		cmp1 = s1+s2
		cmp2 = s2+s1
		if cmp1 > cmp2:
			return 1
		elif cmp2 > cmp1:
			return -1
		return 0

a = [3,32,321]
s = Solution()
print(s.PrintMinNumber(a))