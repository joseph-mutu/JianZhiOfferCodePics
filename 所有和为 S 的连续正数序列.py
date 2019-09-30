#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-07 17:50:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def FindContinuousSequence(self, tsum):
		if tsum <= 2:
			return []
		if tsum == 3:
			return [[1,2]]
		fens = int(tsum/2)+1 
		start,end,curSum = 1,2,3
		totalSeq = []
		while end <= fens:
			if curSum < tsum:
				end += 1
				curSum += end
			if curSum > tsum:
				curSum -= start
				start += 1
			if curSum == tsum and end - start >= 1:
				totalSeq.append(list(range(start,end+1)))
				end += 1
				curSum += end
		return totalSeq
s =Solution()
print(s.FindContinuousSequence(15))