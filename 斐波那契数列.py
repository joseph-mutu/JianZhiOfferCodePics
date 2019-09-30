#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-08-16 07:58:30
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

# import os

class Solution:
	fib = [0,1]
	def Fibonacci(self,n):
		while len(self.fib) <= n:
			self.fib.append(self.fib[-1] + self.fib[-2])
		return self.fib[n]

s = Solution()
print(s.Fibonacci(3))