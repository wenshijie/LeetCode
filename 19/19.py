# -*- coding: utf-8 -*-
"""
Created on =2019-11-08

@author: wenshijie
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        del result[-n]
        head = ListNode(0)
        item = head
        for i in result:
            item.next = ListNode(i)
            item = item.next
        return head.next


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        heads = ListNode(0)
        heads.next=head
        item1 = heads
        i = 1
        while i < n + 1:
            item1 = item1.next
            i += 1
        item2 = heads
        while item1.next is not None:
            item1 = item1.next
            item2 = item2.next
        item2.next= item2.next.next
        return heads.next


if __name__ == "__main__":
    ll = [1]#,2,3,4,5]
    he = ListNode(0)
    it = he
    for i in ll:
        it.next = ListNode(i)
        it = it.next
    S = Solution2()
    head = S.removeNthFromEnd(he.next, 1)
    print(head.val, head.next)
