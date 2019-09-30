#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-19 10:52:22
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def __init__(self):
		self.repeat = False
	def deleteDuplication(self, pHead):
		if not pHead or not pHead.next:
			return pHead
		fakeHead = ListNode(-999)
		fakeHead.next  = pHead

		det1 = fakeHead
		det2 = fakeHead.next

		while det2:
			while det2.next and det2.val == det2.next.val:
				self.repeat = True
				det2 = det2.next
			if self.repeat:
				det1.next = det2.next
				self.repeat = False
				if det2.next:
					det2 = det1.next
				else:
					break
			else:
				det1 = det1.next
				det2 = det2.next

		return fakeHead.next



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(5)
s = Solution()
newHead = s.deleteDuplication(head)
print(newHead)
while newHead:
	print(newHead.val)
	newHead = newHead.next