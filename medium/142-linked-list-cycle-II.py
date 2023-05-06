# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        test = {}
        # a cycle in a linked list jumps back to a previous node. If we keep
        # track of the nodes then we will run into the start of the cycle again
        while head:
            if head not in test:
                test[head] = head.val
                head = head.next
            else:
                return head
