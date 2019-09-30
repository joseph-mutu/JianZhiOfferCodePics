#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-07 14:35:54
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

# string = '123 qwe 2 3' 
# string = list(string)
# num_space = 0

# for i in range(len(string)):
# 	if string[i] == ' ':
# 		num_space += 1
# 	else:
# 		continue

# string2 = ['0' for i in range(num_space*2)]
# string += string2
# last_element = len(string) - num_space*2 - 1
# filler = len(string) - 1

# while num_space > 0:
# 	if string[last_element] == ' ':
# 		num_space -= 1
# 		string[filler] = '0'
# 		string[filler-1] = '2'
# 		string[filler-2] = '%'
# 		filler -= 3
# 		last_element -= 1
# 	else:
# 		string[filler] = string[last_element]
# 		filler -= 1
# 		last_element -= 1
# print(''.join(string))

class Solution:
	def replaceSpace(self,s):
		string = list(s)		
		num_space = 0

		for i in range(len(string)):
			if string[i] == ' ':
				num_space += 1
			else:
				continue

		string2 = ['0' for i in range(num_space*2)]
		string += string2
		last_element = len(string) - num_space*2 - 1
		filler = len(string) - 1

		while num_space > 0:
			if string[last_element] == ' ':
				num_space -= 1
				string[filler] = '0'
				string[filler-1] = '2'
				string[filler-2] = '%'
				filler -= 3
				last_element -= 1
			else:
				string[filler] = string[last_element]
				filler -= 1
				last_element -= 1
		return ''.join(string)

S = Solution()
a = S.replaceSpace("We are happy")
print(a)