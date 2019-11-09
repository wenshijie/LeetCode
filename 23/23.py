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
    def mergeKLists(self, lists: list) -> ListNode:
        head = ListNode(0)
        item = head
        _min1 = float('inf')  # 当前最小
        _min2 = float('inf')  # 下一次循环最小
        while len(lists):
            _list = lists.copy()
            lists.clear()
            for LN in _list:
                if LN is None:  # 防止本来就是空链表 脑子有坑啊
                    continue
                if LN.val == _min1:
                    item.next = ListNode(_min1)
                    item = item.next
                    if LN.next is not None:
                        if LN.next.val < _min2:
                            _min2 = LN.next.val
                        lists.append(LN.next)
                else:
                    if LN.val < _min2:
                        _min2 = LN.val
                    lists.append(LN)
            _min1 = _min2
            _min2 = float('inf')
        return head.next

if __name__ == "__main__":
    # l1 = ListNode(1)
    # l1.next = ListNode(1)
    # l1.next.next = ListNode(2)
    # l2 = ListNode(1)
    # l2.next = ListNode(3)
    # l3 = ListNode(2)
    # l3.next = ListNode(3)
    # l3.next.next = ListNode(4)
    S = Solution()
    h = S.mergeKLists([])
    while h is not None:
        print(h.val)
        h = h.next
