#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-06 18:33:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$
# -*- coding:utf-8 -*-

import numpy as np



# class TreeNode:
#     def __init__(self, x):
#         self.val = x	
#         self.left = None
#         self.right = None
# # class Solution:
# # 	# 返回构造的TreeNode根节点
# def binaryTree(preStart,midStart,length,cur_node):
# 	if length == 0:
# 		return 
# 	if length == 1:
# 		return 
# 	cur_pre = pre[preStart]
# 	mid_index = tin.index(cur_pre)

# 	left_length = mid_index - midStart
# 	right_length = length - left_length - 1

# 	if left_length > 0:
# 		cur_node.left = TreeNode(pre[preStart+1])
# 	if right_length > 0:
# 		cur_node.right = TreeNode(pre[preStart + left_length + 1])
# 	binaryTree(preStart + 1, midStart, left_length,cur_node.left)
# 	binaryTree(preStart + left_length + 1,midStart + left_length + 1,right_length,cur_node.right)

# 	return cur_node




class TreeNode:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None

class Solution:

	def binaryTree(self,preStart,midStart,length,cur_node,pre,tin):
		if length == 0:
			return 
		if length == 1:
			cur_node.left = None
			cur_node.right = None
			return 
		cur_pre = pre[preStart]
		mid_index = tin.index(cur_pre)

		left_length = mid_index - midStart
		right_length = length - left_length - 1

		if left_length > 0:
			cur_node.left = TreeNode(pre[preStart+1])
		if right_length > 0:
			cur_node.right = TreeNode(pre[preStart + left_length + 1])
		self.binaryTree(preStart + 1, midStart, left_length,cur_node.left,pre,tin)
		self.binaryTree(preStart + left_length + 1,midStart + left_length + 1,right_length,cur_node.right,pre,tin)

		return cur_node

	def reConstructBinaryTree(self,pre,tin):
		start_node = TreeNode(pre[0])
		tem = self.binaryTree(0,0,len(pre),start_node,pre,tin)
		return tem

# start_node = TreeNode(pre[0])
# pre = [1,2,3,4,5,6]
# tin = [3,2,4,1,6,5]
sol = Solution()
a = sol.reConstructBinaryTree([1,2,3,4,5,6],[3,2,4,1,6,5])
# a = binaryTree(0,0,len(pre),start_node)
# print(a.val)
# print(a.left.val)
# print(a.right.val)
# print(a.left.left.val)
# print(a.left.right.val)
# print(a.right.left.val)