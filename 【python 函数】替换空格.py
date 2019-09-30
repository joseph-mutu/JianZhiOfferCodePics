#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-07 13:47:07
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ','%20')
        return s