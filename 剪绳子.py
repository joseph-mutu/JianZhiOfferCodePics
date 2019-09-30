#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-27 20:36:45
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def __init__(self):
		self.max_product = [0,1,2,3]
	def cutRope(self, number):
		if number <= 0:
			return None
		if number == 2:
			return 1
		if number == 3:
			return 2
		if number == 4:
			return 4
		num_3 = int(number/3)
		print(num_3)
		return pow(3,num_3)*self.max_product[number%3]
	# def cutRope(self, number):
		# 动态规划
		# if number <=0 :
		# 	return None
		# if number == 2:
		# 	return 1
		# if number == 3:
		# 	return 2
		# for i in range(4,number+1):
		# 	tem_max = 0
		# 	for j in range(1,int(i/2)+1):
		# 		tem = self.max_product[j] * self.max_product[i-j]
		# 		if tem > tem_max:
		# 			tem_max = tem
		# 	self.max_product.append(tem_max)
		# return self.max_product[number]
s = Solution()
print(s.cutRope(5))


