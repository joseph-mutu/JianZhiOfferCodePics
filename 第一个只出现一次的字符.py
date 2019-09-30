#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-09-02 18:50:44
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os

class Solution:
	def FirstNotRepeatingChar(self, s):
		not_repeat = {}
		if s is None:
			return -1
		s = list(s)
		for char in s:
			if not_repeat.get(char) is not None:
				not_repeat[char] += 1
			else:
				not_repeat[char] = 1
		for key_val in not_repeat.items():
			print(key_val[1])
			if key_val[1] == 1:
				for i in range(len(s)):
					if s[i] == key_val[0]:
						return i
		return -1

s = Solution()
repeatChar = "google"
print(s.FirstNotRepeatingChar(repeatChar))