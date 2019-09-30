#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-26 15:27:30
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
	totalDic = {}
	def Clone(self, pHead):
		if not pHead:
			return None
		# write code here
		newHead = self.CreateNewNodes(pHead)
		self.ConnextRandomPoint(pHead,newHead)
		return newHead

	def CreateNewNodes(self,pHead):
		head =RandomListNode(pHead.label)
		newHead = head
		self.totalDic[pHead] = newHead
		pHead = pHead.next
		while pHead:
			temNode = RandomListNode(pHead.label)
			self.totalDic[pHead] = temNode
			newHead.next = temNode
			pHead = pHead.next
			newHead = newHead.next
		return head

	def ConnextRandomPoint(self,pHead,newHead):
		while newHead:
			if pHead.random:
				newHead.random = self.totalDic[pHead.random]
			pHead = pHead.next
			newHead = newHead.next
		return

a = RandomListNode(1)
a.next = RandomListNode(4)
a.next.next = RandomListNode(5)
a.next.next.next = RandomListNode(7)
a.next.next.next.next = RandomListNode(9)
a.random = a.next.next
a.next.random = a.next.next.next.next

s = Solution()
newHead = s.Clone(a)
print(newHead.next.random.label)