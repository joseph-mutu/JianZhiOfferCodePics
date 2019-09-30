#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 19:43:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def ReverseSentence(self, s):
		if len(list(set(s))) == 1 and list(set(s))[0] == " ":
			return s
		if not s:
			return ''
		s = self.ReverseString(s,0,len(s)-1)
		s = s.split(' ')
		count = 0
		for string in s:
			s[count] = self.ReverseString(string,0,len(string)-1)
			count += 1
		return ' '.join(s)

	def ReverseString(self,s,start,end):
		# if s is "":
		# 	return s
		s = list(s)
		if not s:
			return None
		if start > end:
			print("RE-Enter the start and end")
			return None
		while start < end:
			tem = s[start]
			s[start] = s[end]
			s[end] = tem
			start += 1
			end -= 1
		return ''.join(s)

s = Solution()
print(s.ReverseSentence('   '))