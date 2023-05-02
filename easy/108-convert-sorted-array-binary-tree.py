# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # Oof what a doozy. basically the thought process here is to
        # find the middle of the array
        # use that as our root
        # split the array to everything left and everything right
        # our left and right children of the root are the outsides of the
        # array eg [0,x,x,x,x,2] where those are the numbers we care about
        # AFTER the split
        # recursively call the function to repeat the process as long as there
        # are still pieces of the array to work with...
        # whew
        def construct(l, r):
           if l > r:
               return None
           # find mid
           mid = (l +r) // 2

           root = TreeNode(val=nums[mid])
           
           root.left = construct(l, mid-1)

           root.right = construct(mid+1, r)
           return root
        
        return construct(0,len(nums)-1)
