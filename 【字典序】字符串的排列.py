#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-29 20:56:06
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution:

	def Swap(self,ss,pos1,pos2):
		tem = ss[pos1]
		ss[pos1] = ss[pos2]
		ss[pos2] = tem
		return ss
	def ReverseOrder(self,ss,start):
		ss[start:] = ss[len(ss)-1:start:-1]
		return ss


	def Permutation(self,ss):
		self.permu = []
		ss = list(ss)
		firstDown = -1
		firstLargerFirstDown = -1
		ascending = False
		# while not ascending:
		for i in range(len(ss)-2,-1,-1):
			if ss[i] < ss[i+1]:
				firstDown = i
				break
		if firstDown != -1:
			for i in range(i+1,len(ss)):
				if ss[i] < ss[firstDown]:
					firstLargerFirstDown = i-1
					break
		ss = self.Swap(ss,firstDown,firstLargerFirstDown)
		print(ss)
		ss = self.ReverseOrder(ss,firstDown+1)
		return ss

s = Solution()
print(s.Permutation([3,4,6,9,8,7,5,2,1]))