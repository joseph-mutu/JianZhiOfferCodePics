#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-09 18:54:23
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
class Solution:
	def LastRemaining_Solution(self, n, m):
		if n == 0 or m == 0:
			return -1
		last_num = 0
		cur_ite = 2
		while cur_ite <= n:
			last_num = (last_num+m)%cur_ite
			cur_ite += 1
		return last_num

s = Solution()
print(s.LastRemaining_Solution(6,9))

