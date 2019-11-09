# -*- coding: utf-8 -*-
"""
Created on =2019-11-09

@author: wenshijie
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        item = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                item.next = ListNode(l2.val)
                l2 = l2.next
            else:
                item.next = ListNode(l1.val)
                l1 = l1.next
            item = item.next
        if l1 is None:
            item.next = l2
        else:
            item.next = l1
        return head.next

if __name__=="__main__":
    l1 = ListNode(1)
    l1.next=ListNode(2)
    l1.next.next=ListNode(3)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    S=Solution()
    h = S.mergeTwoLists(l1,l2)
    while h is not None:
        print(h.val)
        h = h.next