#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-28 17:22:51
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
	def Convert(self,pRootOfTree):

		if not pRootOfTree:
			return None
		if not pRootOfTree.left and not pRootOfTree.right:
			preNode = pRootOfTree
			return pRootOfTree
		curLeft = self.Convert(pRootOfTree.left)
			
		if curLeft:
			while curLeft.right:
				curLeft = curLeft.right
			pRootOfTree.left = curLeft
			curLeft.right = pRootOfTree

		curRight = self.Convert(pRootOfTree.right)
		if curRight:
			while curRight.left:
				curRight = curRight.left
			pRootOfTree.right = curRight
			curRight.left = pRootOfTree
		while pRootOfTree.left:
			pRootOfTree = pRootOfTree.left
		if pRootOfTree:
			print(pRootOfTree.val)
		return pRootOfTree


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)
s = Solution()
newHead = s.Convert(a)
print(newHead.right.right.val)
