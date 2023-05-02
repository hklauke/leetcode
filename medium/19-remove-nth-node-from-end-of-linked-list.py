# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # For this we can just loop through the linked list n number of times with a temp list and if the temp
        # list == None at the end of "n" loops it means we've reached the end and therefore we are in the correct spot.
        # We then assign the previous node to the next node to remove our current node from the linked list
        # unless we are at the first node, then we can just change first to the next node (which might be None if the list has no more nodes)
        prev = None
        first = head
        while head:
            temp = head
            for i in range(n):
                temp = temp.next
            if temp == None:
                if prev:
                    prev.next = head.next
                elif prev == None:
                    first = head.next      
                return first
            else:
                prev = head
                head = head.next

        return first
                    
