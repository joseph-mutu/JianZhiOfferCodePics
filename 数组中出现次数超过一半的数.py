#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 15:42:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

numbers = [1,3,4,2,4]



class Solution:
	def MoreThanHalfNum_Solution(self, numbers):
		if len(numbers) == 0:
			return 0
		num_count = 0
		target_num = 0
		for num in numbers :
			if num != target_num:
				num_count -= 1
				if num_count < 0:
					num_count = 0
					target_num = num
			else:
				num_count += 1
		if sum([num == target_num for num in numbers]) > int(len(numbers)/2):
			return target_num
		else:
			return 0

s = Solution()
print(s.MoreThanHalfNum_Solution(numbers))
