#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-19 17:36:55
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class ListNode:
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution:
	def FindKthToTail(self, head, k):
		if head is None or k < 1:
			return None
		start = head
		end = head
		stepCount = k
		while stepCount > 1:
			if end.next:
				end = end.next
				stepCount -= 1
			else:
				return None
		while end.next:
			end = end.next
			start  = start.next
		return start



a = ListNode(2)
a.next = ListNode(3)
a.next.next = ListNode(4)
a.next.next.next = ListNode(5)
s = Solution()
print(s.FindKthToTail(a,4).val)