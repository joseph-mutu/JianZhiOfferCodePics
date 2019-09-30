#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-01 19:44:04
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def GetUglyNumber_Solution(self, index):
		if index == 0:
			return 0
		if index <= 6:
			return index
		start = 0
		ugly_number = [1]
		t_2 = 0
		t_3 = 0
		t_5 = 0
		while start < index:
			cur_num = min(ugly_number[t_2]*2,ugly_number[t_3]*3,ugly_number[t_5]*5)
			if cur_num == ugly_number[t_2] *2:
				t_2 += 1
			if cur_num == ugly_number[t_3] *3:
				t_3 += 1
			if cur_num == ugly_number[t_5] *5:
				t_5 += 1
			ugly_number.append(cur_num)
			start += 1
		return ugly_number[index-1]

s = Solution()
print(s.GetUglyNumber_Solution())
