#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-20 19:08:22
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
		self.preorder_traversal = []
		self.inverse_preorder = []
	def isSymmetrical(self, pRoot):
		if not pRoot:
			return True

		self.PreorderTraversal(pRoot)
		self.InversePreorderTraversal(pRoot)
		
		if self.preorder_traversal == self.inverse_preorder:
			return True
		else:
			return False

	def InversePreorderTraversal(self,pRoot):
		if pRoot is None:
			self.inverse_preorder.append('#')
			return 
		self.inverse_preorder.append(pRoot.val)
		self.InversePreorderTraversal(pRoot.right)
		self.InversePreorderTraversal(pRoot.left)

		return 
	def PreorderTraversal(self,pRoot):
		if pRoot is None:
			self.preorder_traversal.append('#')
			return
		self.preorder_traversal.append(pRoot.val)
		self.PreorderTraversal(pRoot.left)
		self.PreorderTraversal(pRoot.right)
		return

s = Solution()
head = TreeNode(8)
head.left = TreeNode(6)
head.right = TreeNode(6)
head.left.left = TreeNode(5)
head.left.right = TreeNode(7)
head.right.left = TreeNode(7)
head.right.right = TreeNode(5)
print(s.isSymmetrical(head))
print(s.preorder_traversal)
print(s.inverse_preorder)