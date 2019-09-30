#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-20 20:12:14
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
	def Print(self, pRoot):
		root = pRoot
		if not root:
			return []
		cur_layer = [root]
		permanent = []
		left_right = -1
		while cur_layer:
			next_layer = []
			tem_permanent = []
			if left_right > 0:
				for node in cur_layer[::-1]:	
					if node.left:
						tem_permanent.append(node.left.val)
						next_layer.append(node.left)
					if node.right:
						tem_permanent.append(node.right.val)
						next_layer.append(node.right)
			else:
				for node in cur_layer[::-1]:	
					if node.right:
						tem_permanent.append(node.right.val)
						next_layer.append(node.right)
					if node.left:
						tem_permanent.append(node.left.val)
						next_layer.append(node.left)	
			if tem_permanent:
				permanent.append(tem_permanent)
			left_right = left_right * -1
			cur_layer = next_layer
		permanent.insert(0,[root.val])
		return permanent



s = Solution()
head = TreeNode(8)
head.left = TreeNode(6)
head.right = TreeNode(10)
head.left.left = TreeNode(5)
head.left.right = TreeNode(7)
head.right.left = TreeNode(9)
head.right.right = TreeNode(11)
print(s.Print(head))