#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-06 18:33:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import numpy as np

pre = [1,2,3,4,5,6]
mid = [3,2,4,1,6,5]
post = list(np.full((6),-1))

def constructBinaryTree(preStart,midStart,posStart,length):
	if length == 0:
		return
	elif length == 1:
		post[posStart] = pre[preStart]
	else:
		cur_pre = pre[preStart]
		mid_pos = mid.index(cur_pre)

		left_length = mid_pos - midStart
		right_length = length - left_length - 1

		post_pos = posStart + length - 1
		post[post_pos] = cur_pre

		constructBinaryTree(preStart+1,midStart,posStart,left_length)
		constructBinaryTree(preStart+left_length+1,midStart + left_length + 1,posStart + left_length,right_length)

constructBinaryTree(0,0,0,len(pre))
print(post)
