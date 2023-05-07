# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def findDepth(root, count):

            if root == None:
                return 0
            
            if not root.left and not root.right:
                return count
            

            left = findDepth(root.left, count+1) 
            right = findDepth(root.right, count +1)
            if left > 0 and right >0:
                return min(left, right)
            else:
                return left +right
            
        
        return findDepth(root, 1)
