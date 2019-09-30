#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-17 20:54:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# 位与运算，只有当两个数的数位均为 1 时，结果才为1

# class Solution:
# 	def Power(self, base, exponent):
# 		if exponent == 0:
# 			return 1
# 		elif exponent == 0:
# 			return 0
# 		ans = 1
# 		curBase = base
# 		negFlag = False
# 		if exponent < 0:
# 			negFlag = True
# 			exponent = -exponent
# 		while exponent:
# 			if exponent & 1:
# 				ans *= curBase
# 			curBase *= curBase
# 			exponent >>= 1
# 		ans = 1/ans if negFlag else ans
# 		return ans
# print(Power(2,4))

class Solution:
	def Power(self, base, exponent):
		if exponent == 0:
			return 1
		if base == 0:
			return 0
		curBase = base
		ans = 1
		negFlag = False
		if exponent < 0:
			exponent = -exponent
			negFlag = True
		while exponent:
			if exponent & 1:
				ans *= curBase
			curBase *= curBase
			exponent >>= 1
		ans = 1/ans if negFlag else ans
		return ans
s = Solution()
print(s.Power(3,3))