#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 18:43:01
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def NumberOf1Between1AndN_Solution(self, n):
		m = 1
		count_1 = 0
		while m <= n:
			a = int(n/m)+ 8
			b = n%m + 1 if int(n/m)%10 == 1 else 0
			tem_count = int(a/10) * m + b
			count_1 += tem_count
			m *= 10
		return count_1

s = Solution()
print(s.NumberOf1Between1AndN_Solution(1))