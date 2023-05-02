# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ## find out sum by traversing the list
        # we're starting out with the totals in reverse [9,0,7] == 709
        # so we can multply by 10 * 10 to whatever loop we are in. in order to
        # get the total sum, we can do both at the same time here to find the
        # total sum
        count = 0
        lsum =0
        while l1 or l2:
            if l1:
                lsum += l1.val * 10 ** count
                l1 = l1.next
            if l2:
                lsum += l2.val * 10 ** count
                l2 = l2.next
            count +=1

        if lsum == 0:
            return ListNode(0)
        first = None

        # we use mod 10 here to get the last number, and then int divide by 10
        # to remove it
        # keep looping till we hit 0
        # if it's the first node then save it for later, otherwise grab the
        # last number create the next node and move to that node.
        while lsum != 0:
            if not first:
                node = ListNode(lsum %10)
                first = node
            else:
                node.next = ListNode(lsum %10)
                node = node.next
            lsum = lsum // 10
        
        return first
