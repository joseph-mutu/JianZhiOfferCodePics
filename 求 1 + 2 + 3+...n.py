#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-10 19:12:40
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def Sum_Solution(self, n):
		return n and self.Sum_Solution(n-1)+n

s = Solution()
print(s.Sum_Solution(3))