#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 09:19:19
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def jumpFloor(self, number):
		jump = [1,2]
		while len(jump) < number:
			jump.append(jump[-1] + jump[-2])
		return jump[number-1]


s = Solution()
print(s.jumpFloor(4))