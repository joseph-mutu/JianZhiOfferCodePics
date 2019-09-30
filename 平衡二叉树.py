#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-06 18:18:24
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

	def IsBalanced_Solution(self, pRoot):
		if pRoot is None:
			return True
		# print(self.SearchDepth(pRoot))
		if self.SearchDepth(pRoot) == -1:
			return False

		return True

	def SearchDepth(self,pRoot):
		if pRoot is None:
			return 0
		left = self.SearchDepth(pRoot.left)
		if left == -1:
			return -1
		right = self.SearchDepth(pRoot.right)
		if right == -1:
			return -1
		if abs(left-right) > 1:
			return -1
		else:
			return max(left,right) + 1

s = Solution()
a = TreeNode(3)
a.left = TreeNode(4)
a.right = TreeNode(7)
a.left.left = TreeNode(9)
a.left.right = TreeNode(8)
a.right.left = TreeNode(4)
a.right.left.right = TreeNode(6)
print(s.IsBalanced_Solution(a))