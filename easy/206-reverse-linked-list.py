# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            # save next value in list
            temp = head.next
            # change current value to previous
            head.next = prev
            # now previous is the new current value
            prev = head
            # move on to next value
            head = temp

        # we return prev becuase if we returned head it would be None
        return prev
