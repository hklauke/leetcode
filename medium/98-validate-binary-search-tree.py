# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(node, left, right):
            if node == None:
                return True
                
            if not (node.val < right and node.val > left):
                return False
            
            return (helper(node.left, left, node.val) and helper(node.right, node.val, right))
        

        return helper(root, float('-inf'), float('inf'))
