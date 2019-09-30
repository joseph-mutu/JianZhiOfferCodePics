#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-05 19:37:00
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
	
	max_depth = 0
	cur_depth = 0
	def TreeDepth(self, pRoot):
		self.cur_depth += 1
		if pRoot is None:
			if self.cur_depth - 1 > self.max_depth:
				self.max_depth = self.cur_depth - 1
			return self.max_depth
		self.TreeDepth(pRoot.left)
		self.cur_depth -= 1
		self.TreeDepth(pRoot.right)
		self.cur_depth -= 1
		return self.max_depth

# start = TreeNode(1)
# start.left = TreeNode(2)
# start.right = TreeNode(3)
# start.left.left = TreeNode(4)
# start.left.left.right = TreeNode(6)

start = 

s = Solution()
print(s.TreeDepth(start))