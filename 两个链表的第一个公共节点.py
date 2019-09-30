#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-04 14:19:59
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# 自己的想法，先遍历第一个链表，用字典存下每一个节点的值
	# 然后遍历第二个链表，看是否有相同的值在字典中
	# def FindFirstCommonNode(self, pHead1, pHead2):
	# 	dicHead1 = {}
	# 	if pHead1 is None or pHead2 is None:
	# 		return None
	# 	while pHead1:
	# 		dicHead1[pHead1.val] = pHead1
	# 		pHead1 = pHead1.next
	# 	while pHead2:
	# 		if dicHead1.get(pHead2.val):
	# 			return pHead2
	# 		pHead2 = pHead2.next
	# 	return None
class Solution:
	def FindFirstCommonNode(self, pHead1, pHead2):
		lengthHead1,lengthHead2 = 0,0
		start1,start2 = pHead1,pHead2
		while start1:
			lengthHead1 += 1
			start1 = start1.next
		while start2:
			lengthHead2 += 1
			start2 = start2.next
		if lengthHead1 > lengthHead2:
			for i in range(lengthHead1 - lengthHead2):
				pHead1 = pHead1.next
		elif lengthHead2 > lengthHead1:
			for i in range(lengthHead2 - lengthHead1):
				pHead2 = pHead2.next
		while pHead1 and pHead2:
			if pHead1.val == pHead2.val:
				return pHead1
			pHead1 = pHead1.next
			pHead2 = pHead2.next
		return None


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = a.next.next
# b.next.next.next = ListNode(6)
s = Solution()
print(s.FindFirstCommonNode(a,b).val)