#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-13 18:11:29
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
 
class Solution:
	def minNumberInRotateArray(self, rotateArray):
		point1 = 0
		point2 = len(rotateArray) - 1
		midIndex = int((point1 + point2)/2)
		if len(rotateArray) == 0:
			return 0
		elif rotateArray[point1] < rotateArray[point2]:
			return rotateArray[point1]
		elif rotateArray[midIndex] == rotateArray[point1] and rotateArray[midIndex] == rotateArray[point2]:
			return min(rotateArray)
		else:
			while point2 - point1 > 1:
				if rotateArray[midIndex] >= rotateArray[point1]:
					point1 = midIndex
				elif rotateArray[midIndex] <= rotateArray[point2]:
					point2 = midIndex
				midIndex = int((point1 + point2)/2)
			return rotateArray[point2]


a = [1,1,1,0,1]
def minNumberInRotateArray():

print(minNumberInRotateArray())

