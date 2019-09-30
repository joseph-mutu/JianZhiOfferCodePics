#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-08 18:59:48
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def LeftRotateString(self, s, n):
		n = n%len(s)
		if not s:
			return ""
		reversed_string = self.ReverseString(s,0,len(s)-1)
		first_reversed = self.ReverseString(reversed_string,0,len(s)-n-1)
		second_reversed = self.ReverseString(first_reversed,len(s)-n,len(s)-1)
		return second_reversed

	def ReverseString(self,string,start,end):
		string = list(string)
		if string is None:
			return None
		if start >= end:
			print("The start and end are wrong")
		while start < end:
			tem = string[start]
			string[start] = string[end]
			string[end] = tem
			start += 1
			end -= 1
		return "".join(string)

s = Solution()
print(s.LeftRotateString("abcdefg",10))

