#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-07 19:09:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def FindNumbersWithSum(self, array, tsum):
		if array is None:
			return []
		start,end = 0,len(array) - 1
		sumOfTwoNum = []
		productOfTwoNum = 99999
		while start < end:
			if array[start] +array[end] == tsum:
				if productOfTwoNum > array[start]*array[end]:
					productOfTwoNum = array[start]*array[end]
					sumOfTwoNum = []
					sumOfTwoNum.append(array[start])
					sumOfTwoNum.append(array[end])
				start += 1
			if array[start] +array[end] > tsum:
				end -= 1
			if array[start] + array[end] < tsum:
				start += 1
		return sumOfTwoNum

s = Solution()
data = [1,2,4,7,11,15]
print(s.FindNumbersWithSum(data,15))