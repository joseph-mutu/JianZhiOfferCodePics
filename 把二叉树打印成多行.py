#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-21 08:08:24
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
	# def Print(self, pRoot):
	# 	if not pRoot:
	# 		return []
	# 	cur_layer = [pRoot]
	# 	res = []
	# 	while cur_layer:
	# 		tem_res = []
	# 		next_layer = []
	# 		for node in cur_layer:
	# 			tem_res.append(node.val)
	# 			if node.left:
	# 				next_layer.append(node.left)
	# 			if node.right:
	# 				next_layer.append(node.right)
	# 		cur_layer = next_layer
	# 		if tem_res:
	# 			res.append(tem_res)
	# 	return res

	def __init__(self):
		self.final_sequence = []
	def Print(self,pRoot):
		# 递归版本
		if not pRoot:
			return self.final_sequence
		self.Preorder(pRoot,1)
		return self.final_sequence

	def Preorder(self,pRoot,depth):
		if not pRoot:
			return
		if depth > len(self.final_sequence):
			self.final_sequence.append([])
		self.final_sequence[depth-1].append(pRoot.val)

		self.Preorder(pRoot.left,depth + 1)
		self.Preorder(pRoot.right,depth + 1)



s = Solution()
head = TreeNode(8)
head.left = TreeNode(6)
head.right = TreeNode(10)
head.left.left = TreeNode(5)
head.left.right = TreeNode(7)
head.right.left = TreeNode(9)
head.right.right = TreeNode(11)
print(s.Print(head))




