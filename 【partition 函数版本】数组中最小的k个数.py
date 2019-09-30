#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-30 17:13:56
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import random

class Solution:

	def GetLeastNumbers_Solution(self, tinput, k):
		k_least = []
		if len(tinput) <= 0 or k <= 0 or k > len(tinput):
			return []
		end = len(tinput) - 1
		index = self.Partition(tinput,0,end)
		start = 0
		while index != k-1:
			if index > k - 1:
				end = index - 1
				index = self.Partition(tinput,start,end)
			if index < k - 1:
				start = index+1
				index = self.Partition(tinput,start,end)
		k_least = tinput[:k]
		return sorted(k_least)

	def Partition(self,tinput,start,end):
		index = random.randint(start,end)
		self.Swap(tinput,index,end)
		small_index = start
		big_index = end - 1
		while 1:
			while tinput[small_index] <= tinput[end] and small_index < end:
				small_index += 1
			while tinput[big_index] >= tinput[end] and big_index > 0:
				big_index -= 1
			if small_index < big_index:
				self.Swap(tinput,small_index,big_index)
			else:
				break
		self.Swap(tinput,small_index,end)
		return small_index
	def Swap(self,tinput,pos1,pos2):
		tem  = tinput[pos1]
		tinput[pos1] = tinput[pos2]
		tinput[pos2] = tem



tinput = [2,3,1,4,2,1,23,4]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput,4))