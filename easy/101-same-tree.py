# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True

        left,right = [], []
        # this is basically the same as symmetric tree except i can traverse
        # the trees in the same direction both times and therefore don't need
        # any extra conditionals.
        def traverse(root,stack):
            if root == None:
                stack.append(None)
                return
            stack.append(root.val)
            traverse(root.left, stack)
            traverse(root.right, stack)
           

        traverse(p, left)
        traverse(q, right)
            
       
        if left == right:
            return True
        return False
