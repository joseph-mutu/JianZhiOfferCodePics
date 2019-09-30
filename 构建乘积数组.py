#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-17 10:57:26
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def multiply(self, A):
		if not A:
			return []
		left_top_bottom = [1]
		right_bottom_top = [1]

		len_limit = len(A)
		for i in range(1,len_limit):
			left_top_bottom.append(left_top_bottom[i-1] * A[i-1])
			right_bottom_top.append(right_bottom_top[i-1] * A[len_limit-i])

		B = []
		for i in range(0,len_limit):
			B.append(left_top_bottom[i] * right_bottom_top[len_limit-1-i])
		return B


s = Solution()
A = [1,0,3,4]
print(s.multiply(A))


