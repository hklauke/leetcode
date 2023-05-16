# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = ListNode()
        head = merged

        # compare values, add one at a time to new list, was we exit there will be one node left, add that and return our head without the dummy node

        while list1 and list2:

            if list1.val <= list2.val:
               merged.next = list1
               list1 = list1.next
            else:
                merged.next = list2
                list2 = list2.next
            
            merged = merged.next    

        if list1:
            merged.next = list1
        else:
            merged.next = list2
        
        return head.next
