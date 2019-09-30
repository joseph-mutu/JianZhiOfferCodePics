#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-24 09:04:51
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

class Solution:
	def VerifySquenceOfBST(self, sequence):
		if not sequence:
			print(sequence)
			return False
		return self.judge(sequence)
	def judge(self,sequence):
		if not sequence:
			return True
		curRoot = sequence[-1]
		del sequence[-1]
		rightRoot = len(sequence)-1
		leftTree = []
		rightTree = []
		for i in range(len(sequence)):
			if sequence[i] < curRoot:
				leftTree.append(sequence[i])
			else:
				rightRoot = i
				break
		if len(leftTree) != len(sequence):
			rightTree = sequence[rightRoot:]
			for j in range(rightRoot,len(sequence)):
				if sequence[j] < curRoot:
					return False
		return self.judge(leftTree) and self.judge(rightTree)


# a = [7,4,6,5]
a = [2,1,5,9,7,4,3]
s = Solution()
print(s.VerifySquenceOfBST(a))