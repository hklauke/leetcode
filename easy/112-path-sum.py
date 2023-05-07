# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        def getSum(root, mysum):
            if root == None:
                return False

            mysum = mysum + root.val

            if not root.left and not root.right:
                return mysum == targetSum
            res = getSum(root.left, mysum) or getSum(root.right, mysum)
            return res
        
        return getSum(root, 0)
