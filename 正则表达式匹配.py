#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-17 18:10:15
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def match(self,s,pattern):
		if len(s) == 0 and len(pattern) == 0:
			return True
		elif len(s) == 0 and len(pattern) > 1:
			if pattern[1] == "*":
				return self.match(s,pattern[2:])
			else:
				return False
		elif len(s) > 0 and len(pattern) == 0:
			return False
		else:
			# s is not None and pattern is not None
			if len(pattern) > 1 and pattern[1] == "*":
				if s[0] != pattern[0] and pattern[0] != ".":
					return self.match(s,pattern[2:])
				else:
					return self.match(s,pattern[2:]) or self.match(s[1:],pattern) 
			elif len(s) > 0 and ( pattern[0] == "." or s[0] == pattern[0]):
				return self.match(s[1:],pattern[1:])				
		return False
s = Solution()
print(s.match(""," "))

# or self.match(s[1:],pattern[2:])