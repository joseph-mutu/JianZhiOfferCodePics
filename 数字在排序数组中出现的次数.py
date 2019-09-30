#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-04 18:08:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def GetNumberOfK(self, data, k):
		if not data:
			return 0
		k_count_left,k_count_right = 0,0
		k_count_left = self.SearchNumberPos(data,k-0.5) 
		k_count_right = self.SearchNumberPos(data,k+0.5)
		print(k_count_left,k_count_right)
		return k_count_right - k_count_left

	def SearchNumberPos(self,data,num):
		start,end = 0,len(data)-1
		mid = int( (start + end)/2)

		while start <= end:
			if data[mid] < num:
				start = mid + 1
			if data[mid] > num:
				end = mid - 1
			mid = int( ( start + end) / 2)
		return start

 
data = [1,2,3,3,3,3,4,5,6,7,8]
s = Solution()
print(s.GetNumberOfK(data,3))