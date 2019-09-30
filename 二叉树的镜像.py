#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-21 15:23:53
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
	def Mirror(self, root):
		if root is None:
			return None
		if root.left and root.right:
			tem = root.right
			root.right = root.left
			root.left = tem
			root.left = self.	Mirror(root.left)
			root.right = self.Mirror(root.right)
		elif root.left:
			root.right = root.left
			root.left = None
			root.right = self.Mirror(root.right)
		elif root.right:
			root.left = root.right
			root.right = None
			root.left = self.Mirror(root.left)
		return root
a = TreeNode(8)
# a.left = TreeNode(6)
a.left = None
a.right = TreeNode(10)
a.right.right = TreeNode(11)
# a.left.right = TreeNode(12)


s = Solution()
print(s.Mirror(a).left.left.val)

