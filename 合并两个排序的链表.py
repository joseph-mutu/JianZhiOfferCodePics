#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-20 19:29:57
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
#递归版本
	def Merge(self, pHead1, pHead2):
		if pHead1 is None:
			return pHead2
		if pHead2 is None:
			return pHead1
		if pHead1 and pHead2 is None:
			return None
		if pHead1.val <= pHead2.val:
			pHead1.next = self.Merge(pHead1.next,pHead2)
			return pHead1
		else:
			pHead2.next = self.Merge(pHead1,pHead2.next)
			return pHead2
# 非递归版本

	# def Merge(self, pHead1, pHead2):
	# 	if pHead1 is None:
	# 		return pHead2
	# 	if pHead2 is None:
	# 		return pHead1
	# 	if pHead1 and pHead2 is None:
	# 		return None
	# 	if pHead1.val <= pHead2.val:
	# 		newHead = pHead1
	# 		pHead1 = pHead1.next
	# 	else:
	# 		newHead = pHead2
	# 		pHead2 = pHead2.next
	# 	temHead = newHead
	# 	while pHead1 and pHead2:
	# 		if pHead1.val <= pHead2.val:
	# 			newHead.next = pHead1
	# 			pHead1 = pHead1.next
	# 		else:
	# 			newHead.next = pHead2
	# 			pHead2 = pHead2.next
	# 		newHead = newHead.next
	# 	if pHead1:
	# 		newHead.next = pHead1
	# 	else:
	# 		newHead.next = pHead2
	# 	return temHead

a = ListNode(2)
a.next = ListNode(3)
a.next.next = ListNode(6)
b = ListNode(1)
b.next = ListNode(5)

s = Solution()
print(s.Merge(a,b).val)
# print(head.next.next.next.next.next)