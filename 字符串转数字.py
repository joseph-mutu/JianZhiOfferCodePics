#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-12 20:46:18
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def StrToInt(self, s):

		if s == "":
			return 0

		string = list(s)
		legal_dic = ['0','1','2','3','4','5','6','7','8','9','+','-']
		
		string_to_int = 0
		pos_neg = 1

		if s[0] == "+" or s[0] == "-":
			pos_neg = self.Judge_Pos_Neg(string[0])
			string = string[1:]
		print(pos_neg)
		for str in string:
			if str == '+' or str == '-':
				return 0
			if str in legal_dic:
				string_to_int = string_to_int*10 + legal_dic.index(str)
			if str not in legal_dic:
				string_to_int = 0
				return string_to_int
		return string_to_int*pos_neg

	def Judge_Pos_Neg(self,string):
		pos_neg = 1
		if string == '+':
			pos_neg = 1
		if string == '-':
			pos_neg = -1
		return pos_neg
s = Solution()
print(s.StrToInt("-123"))