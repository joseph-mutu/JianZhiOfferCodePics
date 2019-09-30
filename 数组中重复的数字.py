#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-14 09:22:11
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	# 利用额外的散列表寻找重复出现的数字
	# def duplicate(self,numbers,duplication):
	# 	if not numbers:
	# 		return False
	# 	dupli_dic = {}
	# 	for num in numbers:
	# 		if dupli_dic.get(num):
	# 			dupli_dic[num] += 1
	# 			duplication[0] = num
	# 			print(duplication[0])
	# 			return True
	# 		else:
	# 		 dupli_dic[num] = 1
	# 	return False
	# 不使用散列表
	def duplicate(self,numbers,duplication):
		cur_pos = 0
		while cur_pos < len(numbers):
			if numbers[cur_pos] == cur_pos:
				cur_pos +=1
			else:
				if numbers[cur_pos] == numbers[numbers[cur_pos]]:
					print("cur_pos",cur_pos)
					duplication[0] = numbers[cur_pos]
					return True
				else:
					tem = numbers[cur_pos]
					numbers[cur_pos] = numbers[numbers[cur_pos]]
					numbers[tem] = tem
		return False

s = Solution()
print(s.duplicate([0,1,2,3,4,5],[-1]))


