#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 20:10:03
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:	
	def ReverseList(self,pHead):
		if pHead is None:
			return None
		elif pHead.next is None:
			return pHead

		pLast = None
		while pHead:
			pNext = pHead.next
			pHead.next = pLast
			pLast = pHead
			pHead = pNext
		return pLast

# 	def ReverseList(self,pHead):
# 		if pHead is None:
# 			return None
# 		start = pHead
# 		if start.next is None:
# 			return start
# 		mid = start.next
# 		start.next = None
# 		if mid.next is None:
# 			mid.next = start
# 			return mid
# 		end = mid.next
# 		while end.next:
# 			mid.next = start
# 			start = mid
# 			mid = end
# 			end = end.next
# 		mid.next = start
# 		end.next = mid
# 		return end





a = ListNode(2)
a.next = ListNode(3)
a.next.next = ListNode(4)
# a.next.next.next = ListNode(5)
# a.next.next.next.next = ListNode(6)
s = Solution()
newHead = s.ReverseList(a)
print(newHead.val)
