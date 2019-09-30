#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-18 07:06:21
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def isNumeric(self, s):
		if not s:
			return False
		s = list(s)
		neg_pos = ['+','-']
		power = ['E','e']
		dot_count = 0
		for pos in range(len(s)):
			print(pos,s[pos])
			if s[pos] == '.':
				dot_count += 1
				if dot_count > 1:
					return False
			elif s[pos] in neg_pos:
				if pos == 0:
					if len(s) > pos + 1 and s[pos+1] in neg_pos:
						return False
				else:
					if s[pos-1] not in power:
						return False
				continue
			elif s[pos] not in power and s[pos] not in neg_pos and s[pos] != '.' and ( ord(s[pos]) < 48 or ord(s[pos]) > 57):
				return False
			elif s[pos] in power:
				if pos == len(s) - 1:
					return False
				for Epos in range(pos+1,len(s)):
					if s[Epos] in power:
						return False
					elif s[Epos] == '.':
						return False
					elif s[Epos] in neg_pos:
						if s[Epos-1] not in power:
							return False
						continue
					elif s[Epos] < '0' or s[Epos] > '9':
						return False
				return True
		return True


s = Solution()
print(s.isNumeric('e16'))
