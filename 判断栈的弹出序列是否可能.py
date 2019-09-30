#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 09:51:24
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# class Solution:
# 	def IsPopOrder(self, pushV, popV):
# 		if not pushV or not popV:
# 			return False
# 		if not pushV and not popV:
# 			return True
# 		assStack = []
# 		for i in range(len(popV)):
# 			curPop = popV[i]
# 			if not assStack:
# 				if curPop in pushV:
# 					for j in range(pushV.index(curPop)+1):
# 						tem = pushV[0]
# 						assStack.append(tem)
# 						del pushV[pushV.index(tem)]
# 				else:
# 					return False
# 			if assStack and curPop == assStack[-1]:
# 				assStack.pop()	
# 				continue
# 			if assStack and curPop != assStack[-1]:
# 				if curPop in pushV:
# 					# prePopPosInPush = pushV.index(prePop)
# 					curPopPosInPush = pushV.index(curPop)
# 					for j in range(0,curPopPosInPush+1):
# 						assStack.append(pushV[j])
# 					assStack.pop()
# 				else:
# 					return False
# 		return True
				
class Solution:
	def IsPopOrder(self, pushV, popV):
		assStack = []
		popPos = 0
		for i in range(len(pushV)):
			assStack.append(pushV[i])
			while assStack and popV[popPos] == assStack[-1]:
				assStack.pop()
				popPos += 1
		if not assStack:
			return True
		else:
			return False




s = Solution()
a = [1,2,3,4,5]
b = [4,5,3,2,1]
# b = [4,3,5,1,2]
# b = [4]
print(s.IsPopOrder(a,b))
