#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 15:05:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def NumberOf1Between1AndN_Solution(self, n):
		count_1 = 0
		for i in range(1,n+1):
			tem_str = [tem for tem in str(i)]
			for string in tem_str:
				if string == "1":
					count_1 += 1
		return count_1
s = Solution()
print(s.NumberOf1Between1AndN_Solution(31256))

