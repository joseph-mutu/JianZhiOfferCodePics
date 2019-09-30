#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-31 14:37:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def FindGreatestSumOfSubArray(self, array):
		if len(array) <= 0:
			return 0
		maxSum = -9999
		temSum = 0
		for num in array:
			temSum = temSum + num 
			maxSum = temSum if temSum > maxSum else maxSum
			if temSum < 0:
				temSum = 0
		return maxSum

data = [-1,-3,-2,-7,-15,-1,-2,-2]
s = Solution()
print(s.FindGreatestSumOfSubArray(data))