#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-06 20:57:08
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:


	def FindNumsAppearOnce(self, array):
		temB = array[0]
		for i in range(1,len(array)):
			temB = temB^array[i]
		Last1Pos = self.FindLastNumber1(bin(temB))
		if Last1Pos == 1:
			print("输入有误，数组中不存在单独出现的数字")

		array,count = self.SplitArray(array,Last1Pos)
		return self.XORFindIndeNum(array,count)

	def XORFindIndeNum(self,array,count):
		indeNum1 = array[0]
		for i in range(1,count):
			indeNum1 = indeNum1 ^ array[i]
		indeNum2 = array[count]
		for j in range(count+1,len(array)):
			indeNum2 = indeNum2 ^ array[j]
		return [indeNum1,indeNum2]

	def FindLastNumber1(self,bNum):
		tem = bNum[2:]
		for i in range(len(tem)-1,-1,-1):
			if tem[i] == "1":
				return int(i-len(tem))
		return 1

	def SplitArray(self,array,Last1Pos):
		SplitPos = 0
		OperationCount = 0
		curPos = 0
		while OperationCount != len(array):
			if bin(array[curPos])[Last1Pos] != "1":
				array.append(array[curPos])
				del array[curPos]
				OperationCount += 1
			else:
				curPos += 1
		return [array,curPos]

a = [2,3,2,3,5,6,7,5,6,8]
s = Solution()
print(s.FindNumsAppearOnce(a))