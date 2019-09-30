#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-26 09:10:31
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# 返回 RandomListNode
	def Clone(self, pHead):
		if not pHead:
			return None
		# write code here
		self.CloneNodes(pHead)
		self.CloneRanomPointer(pHead)
		return self.SplitChain(pHead)


	def CloneNodes(self,pHead):
		while pHead:
			temNode = RandomListNode(pHead.label)
			temNode.next = pHead.next
			pHead.next = temNode
			pHead = temNode.next
	def CloneRanomPointer(self,pHead):
		while pHead.next.next:
			if pHead.random:
				pHead.next.random = pHead.random.next
			pHead = pHead.next.next
	def SplitChain(self,pHead):
		newHead= pHead.next
		while pHead.next:
			tem = pHead.next
			pHead.next = tem.next
			pHead = tem
		return newHead


a = RandomListNode(1)
a.next = RandomListNode(4)
a.next.next = RandomListNode(5)
a.next.next.next = RandomListNode(7)
a.next.next.next.next = RandomListNode(9)
a.random = a.next.next
a.next.random = a.next.next.next.next
s = Solution()
# while a:
# 	print(a.label)
# 	a = a.next
newHead = s.Clone(a)
print(newHead.label)