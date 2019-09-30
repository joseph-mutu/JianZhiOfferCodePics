#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-09 18:21:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def IsContinuous(self, numbers):
		if not numbers:
			return False
		numbers = sorted(numbers)
		zero_count = 0
		gap_count = 0
		for i in range(len(numbers)):
			if numbers[i] == 0:
				zero_count += 1
				continue
			if i > 0 and numbers[i-1] != 0:
				if numbers[i] - numbers[i-1] == 0:
					return False
				tem_sum = 0 if numbers[i] - numbers[i-1] <= 1 else numbers[i] - numbers[i-1] - 1
				gap_count +=  tem_sum
		print(zero_count,gap_count,numbers)
		if zero_count >= gap_count:
			return True
		return False

s = Solution()
data = []
print(s.IsContinuous(data))
