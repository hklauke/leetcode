# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# beats 95% time, 94% space

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # save first node to use again
        firstA, firstB = headA, headB
        # save last node because if tails are different than they don't intersect
        lastA, lastB = headA, headB
        # looking for len of linked list for later
        lenA, lenB = 0, 0
        # loop until end of Both
        while headA or headB:
            if headA:
                # increase len
                lenA +=1
                # save last 
                if headA.next == None:
                    lastA = headA
                headA = headA.next
            if headB:
                lenB +=1
                if headB.next == None:
                    lastB = headB
                headB = headB.next
        
        # if the tails are different then no intersect
        if lastA != lastB:
            return None
        # we should have the len here so now we need to make these the same size,
        if lenA > lenB:
            for i in range(lenA-lenB):
                firstA = firstA.next
            lenA = lenB
        elif lenA < lenB:
            for i in range(lenB-lenA):
                firstB = firstB.next
            lenB = lenA
        # lens are the same so if they are equal find the intersect
        for i in range(lenA):
            if firstB == firstA:
                return firstB
            else:
                firstB = firstB.next
                firstA = firstA.next
        return None
