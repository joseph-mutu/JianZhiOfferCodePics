#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-24 20:38:23
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
	totalPath = []
	def FindPath(self, root, expectNumber):
		self.totalPath = []
		if root is None:
			return self.totalPath
		self.AddPath(root,expectNumber,[])
		return self.totalPath
	def AddPath(self,root,expectNumber,curPath):
		if root and root.left is None and root.right is None and expectNumber - root.val == 0:
			curPath.append(root.val)
			self.totalPath.append(curPath[:])
			curPath.pop()
			return 
		expectNumber -= root.val
		curPath.append(root.val)
		if root.left and expectNumber - root.left.val >= 0:
			self.AddPath(root.left,expectNumber,curPath)
		if root.right and expectNumber - root.right.val >= 0:
			self.AddPath(root.right,expectNumber,curPath)
		curPath.pop()


s = Solution()
a = None
# a = TreeNode(10)
# a.left = TreeNode(5)
# a.right = TreeNode(12)
# a.left.left = TreeNode(4)
# a.left.right = TreeNode(7)
# a.right.left = TreeNode(5)
# a.right.right = TreeNode(7)

ans = s.FindPath(a,0)
print(ans)
