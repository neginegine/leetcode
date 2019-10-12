# -*- coding: UTF-8 -*-
__author__ = 'Deathy'

'''
https://leetcode-cn.com/problems/
'''

###############################################


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        list_len = 1
        tail = head

        while tail.next is not None:
            list_len += 1
            tail = tail.next

        k = k % list_len if list_len > 0 else 0

        new_head = head

        if k > 0:

            new_tail = head

            for i in range(list_len - k - 1):
                new_tail = new_tail.next

            new_head = new_tail.next

            tail.next = head
            new_tail.next = None

        return new_head


###############################################

head = ListNode(1)
point = head
point.next = ListNode(2)
point = point.next
point.next = ListNode(3)
point = point.next
point.next = ListNode(4)
point = point.next
point.next = ListNode(5)

s = Solution()

new_list = s.rotateRight(head, 2)

while new_list is not None:
    print(new_list.val)
    new_list = new_list.next
