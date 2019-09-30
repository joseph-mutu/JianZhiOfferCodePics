#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 18:45:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:

	def __init__(self):
		self.midorder_traversal = []

	def KthNode(self, pRoot, k):
		if not pRoot:
			return None
		if k <= 0:
			return None
		self.MidorderTraversal(pRoot)
		if k <= len(self.midorder_traversal):
			return self.midorder_traversal[k-1]
		else:
			return None

	def MidorderTraversal(self,pRoot):
		if not pRoot:
			return 
		self.MidorderTraversal(pRoot.left)
		self.midorder_traversal.append(pRoot)
		self.MidorderTraversal(pRoot.right)

		return 




head = TreeNode(8)
head.left = TreeNode(6)
head.right = TreeNode(10)
head.left.left = TreeNode(5)
head.left.right = TreeNode(7)
head.right.left = TreeNode(9)
head.right.right = TreeNode(11)

s = Solution()
print(s.KthNode(head,1))