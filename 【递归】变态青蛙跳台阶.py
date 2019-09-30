#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 09:37:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class Solution:
	def jumpFloorII(self, number):
		jump = [1,1,2]
		ans = 4
		if number <=2 :
			return jump[number]
		while len(jump) <= number:
			jump.append(ans)
			ans += jump[-1]
		return jump[-1]

s = Solution()
print(s.jumpFloorII(4))