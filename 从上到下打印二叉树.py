#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-23 16:41:17
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
	def PrintFromTopToBottom(self, root):
		if root is None:
			return []
		nodes = []
		nodes.append(root)
		nodeCount = 0
		while nodeCount < len(nodes):
			if nodes[nodeCount].left is not None:
				nodes.append(nodes[nodeCount].left)
			if nodes[nodeCount].right is not None:
				nodes.append(nodes[nodeCount].right)
			nodes[nodeCount] = nodes[nodeCount].val
			nodeCount += 1
		return nodes

a = TreeNode(2)
a.left = TreeNode(3)
a.left.left = TreeNode(7)
a.left.left.left = TreeNode(9)
# a.right = TreeNode(7)
# a.left.left = TreeNode(4)
# a.right.left = TreeNode(5)
# a.right.right = TreeNode(9)
s = Solution()
print(s.PrintFromTopToBottom(a))
print()