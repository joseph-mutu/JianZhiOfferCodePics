#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-22 07:54:12
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
		self.series = []
		self.DesHead = None
		self.count = 0

	def Serialize(self, root):
		if root and not root.left and not root.right:
			self.series.append(root.val)
			self.series.append('!')
			return self.series
		if not root:
			self.series.append('#')
			return self.series
		self.series.append(root.val)
		self.series = self.Serialize(root.left)
		self.series = self.Serialize(root.right)
		return self.series

	def Deserialize(self, s):
		if s:
			if s[self.count] != '#' and s[self.count] != '!':
				self.DesHead = self.DeserializeProcess(s,self.DesHead)
		return self.DesHead

	def DeserializeProcess(self,s,head):
		if self.count < len(s):
			head = TreeNode(int(s[self.count]))
			self.count += 1
			if s and s[self.count] == '!':
				self.count += 1
				return head
			else:
				if s[self.count] != '#':
					head.left = self.DeserializeProcess(s,head.left)
				else:
					self.count += 1
				if s[self.count] != '#':
					head.right = self.DeserializeProcess(s,head.right)
				else:
					self.count += 1
		return head

head = TreeNode(1)
head.left = TreeNode(2)
# head.right = TreeNode(3)
head.left.left = TreeNode(4)
# head.right.left = TreeNode(5)
# head.right.right = TreeNode(6)
head.left.left.left = TreeNode(6)


s = Solution()
print(s.Serialize(head))
print(s.Deserialize(s.series).left.val)
# print(s.Deserialize(s.series).val)
