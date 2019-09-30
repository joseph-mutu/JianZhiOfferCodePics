#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-07-06 18:33:25
# @Author  : mutudeh (josephmathone@gmail.com)
# @Link    : ${link}
# @Version : $Id$

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 	def search(self,num):
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        tem_list = []
        while listNode:
        	tem_list.append(listNode.val)
        	listNode = listNode.next
        tem_list.reverse()
        return tem_list


class Solution:
    # # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
        	return []
        else:
        	return self.printListFromTailToHead(listNode.next) + [listNode.val]

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
sol = Solution()
tem = sol.printListFromTailToHead(a)
print(tem)

