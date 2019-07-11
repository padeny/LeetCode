#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def get_int(self, l: ListNode)->int:
        m, n = 0,0
        while l is not None:
            m += l.val * 10 ** n
            n += 1
            l = l.next
        return m

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_int = self.get_int(l1)
        l2_int = self.get_int(l2)
        r = l1_int + l2_int

        #[8,0,7]
        b = None
        for i in list(map(int,list(str(r)))):
            a = ListNode(i)
            a.next = b
            b = a
        return a

