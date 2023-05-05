# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # linked list placeholders
        first = head
        prev = None
        # we're always comparing to the last node so if it's empty just move on
        # if the last node is the same as the current then last nodes next is going to skip the current node
        # we have to make sure we increment prev if there is no match otherwise it will just compare to the last duplicate and not the prev node
        while head:
            if not prev:
                prev = head
            elif prev.val == head.val:
                prev.next = head.next
            else:
                prev = prev.next
            
            head = head.next
            
        return first
