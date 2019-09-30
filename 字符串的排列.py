#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-29 17:52:58
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def Permutation(self, ss):
		self.permu = []
		if ss:
			ss = list(ss)
			self.Permutation_process(ss,0,len(ss))
		return sorted(self.permu)

	def Permutation_process(self,ss,start,end):
		if start == end - 1:
			self.permu.append("".join(ss[:]))
			return 
		for i in range(start,end):
			if self.Is_swap(ss,start,i):
				ss = self.Swap(ss,start,i)
				self.Permutation_process(ss,start+1,end)
				ss = self.Swap(ss,start,i)

	def Is_swap(self,ss,start,end):
		for i in range(start,end):
			if ss[i] == ss[end]:
				return False
		return True

	def Swap(self,ss,pos1,pos2):
		tem = ss[pos1]
		ss[pos1] = ss[pos2]
		ss[pos2] = tem
		return ss

s = Solution()
strings = ["abc"]
for sen in strings:
	print(s.Permutation(sen))