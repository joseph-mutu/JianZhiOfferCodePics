#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 18:27:36
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
		self.is_circle_chain = False
		self.chain_length = 0

	def EntryNodeOfLoop(self, pHead):
		if not pHead or not pHead.next:
			return None
		self.IsChain(pHead)
		if not self.is_circle_chain:
			return None

		det_entry1 = pHead
		det_entry2 = pHead
		for i in range(self.chain_length):
			det_entry2 = det_entry2.next
		while det_entry1 != det_entry2:
			det_entry1 = det_entry1.next
			det_entry2 = det_entry2.next
		return det_entry1
	def IsChain(self,pHead):
		det1 = pHead
		det2 = pHead.next
		while det1 and det2 and det1 != det2:
			det1 = det1.next
			det2 = det2.next
			if det2:
				det2 = det2.next
		if det1 == det2:
			self.is_circle_chain = True
		if self.is_circle_chain:
			self.chain_length += 1
			det1 = det1.next
			while det1 != det2:
				det1 = det1.next
				self.chain_length += 1
		return


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
s = Solution()
if s.EntryNodeOfLoop(head) is not None:
	print(s.EntryNodeOfLoop(head).val)
else:
	print(s.EntryNodeOfLoop(head))

