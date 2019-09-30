#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-20 06:45:22
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
	def GetNext(self, pNode):
		if not pNode:
			return pNode
		if pNode.right:
			return self.SearchEnd(pNode.right)
		else:
			if pNode.next:
				# 如果当前的节点是左儿子
				if pNode.next.left and pNode.next.left.val == pNode.val:
					return pNode.next
				# 如果当前节点是右儿子
				elif pNode.next.right and pNode.next.right.val == pNode.val:
					return self.SearchLeftFather(pNode.next)
			else:
				return None

	def SearchEnd(self,curNode):
		if curNode.left is None and curNode.right is None:
			return curNode
		if curNode.left:
			return self.SearchEnd(curNode.left)
		else:
			return curNode

	def SearchLeftFather(self,curNode):
		if curNode.next:
			if curNode.next.left and curNode.next.left.val == curNode.val:
				return curNode.next
			else:
				return self.SearchLeftFather(curNode.next)
		else:
			return None




head = TreeLinkNode(1)
head.next = None
head.left = TreeLinkNode(2)
head.left.next = head
head.right = TreeLinkNode(3)
head.right.next = head
head.left.left = TreeLinkNode(4)
head.left.left.next = head.left
head.left.right = TreeLinkNode(5)
head.left.right.next = head.left
head.left.left.left = TreeLinkNode(6)
head.left.left.left.next = head.left.left
head.left.left.right = TreeLinkNode(11)
head.left.left.right.next = head.left.left
head.left.right.left = TreeLinkNode(13)
head.left.right.left.next = head.left.right
head.left.right.left.right = TreeLinkNode(17)
head.left.right.left.right.next = head.left.right.left
head.left.right.right = TreeLinkNode(7)
head.left.right.right.next = head.left.right
head.right.right = TreeLinkNode(9)
head.right.right.next = head.right


s = Solution()
a = s.GetNext(head.left.right.right )
if a:
	print(a.val)
else:
	print(a)
