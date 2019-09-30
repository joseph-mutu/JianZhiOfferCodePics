#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-03 09:34:53
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	Inverse_count = 0
	def InversePairs(self,data):
		if len(data) == 1:
			return data
		divide_length = 1
		data_length = len(data)
		while divide_length < data_length:
			copy_data = data[:]
			rest_length = data_length % (2*divide_length)
			i = 0
			while i < data_length - rest_length:
				data = self.Merge_process(data,copy_data,i,i+divide_length,i+2*divide_length-1)
				i = i+2*divide_length
			if rest_length > divide_length:
				# 说明遗留下来的不止一个子列
				left = data_length - rest_length
				right = left + divide_length
				end_right = data_length - 1
				data = self.Merge_process(data, copy_data, left , right, end_right)
			divide_length *= 2
		return self.Inverse_count


	def Merge_process(self,data,copy_data,start_left,start_right,end_right):

		end_left = start_right - 1
		copy_count = start_left

		# 进行两个子数组的合并
		while start_left <= end_left and start_right <= end_right:
			# print("data",data)
			# print("copy_data",copy_data)
			# print(start_left,start_right,end_left,end_right)
			if data[start_left] > data[start_right]:
				# 如果最左边的数大于右边的某个数，相当于
				# 所有左边之后的数都大于右边的这个数，都构成了逆序对
				self.Inverse_count += end_left - start_left + 1
				copy_data[copy_count] = data[start_right]
				start_right += 1
			elif data[start_left] < data[start_right]:
				copy_data[copy_count] = data[start_left]
				start_left += 1
			copy_count += 1
		if start_left > end_left:
			copy_data[copy_count:end_right+1] = data[start_right:end_right+1]
		if start_right > end_right:
			copy_data[copy_count:end_right+1] = data[start_left:end_left+1]

		data = copy_data[:]
		return data


data = [2,3,9,12,7,4,5,8,10]
s = Solution()
print(s.Merge_sort(data))
# data [2, 3, 9, 12, 4, 7, 4, 5, 8, 10]
# copy_data [2, 3, 9, 12, 4, 7, 4, 5, 8, 10]
# 4 6 5 7
