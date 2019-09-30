#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-10 20:39:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution:
	def Add(self, num1, num2):
		while num2 != 0: 
			sum_without_carry = (num1^num2) & 0xffffffff
			num2 = ((num1 & num2) << 1) & 0xffffffff
			num1 = sum_without_carry 
		return num1 if num1 >> 31 == 0 else num1 - 4294967296
s = Solution()
print(s.Add(-1,-1))