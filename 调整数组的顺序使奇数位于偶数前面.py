#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-18 09:52:47
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def reOrderArray(self,array):
		count = len(array)
		curPos = 0
		while count:
			count -= 1
			if array[curPos] & 1:
				curPos += 1
				continue
			else:
				array.append(array[curPos])
				del array[curPos]
		return array
s = Solution()
print(s.reOrderArray([1,2,3,4,0]))