# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # we need to find if the depth of the two sub tress of a node differ by more than one
        # if we can find subtree depth of left and right and compare how deep they are  that will determine if they are height balanced
        ans = [True]
        
        # Recursive dfs
        def dfs(root):
            if root == None:
                return 0
                
            l = dfs(root.left) # find height of left tree
            r = dfs(root.right) # find heeight of right tree
            diff = abs(l-r) # find diff in heights

            if diff > 1:
                ans[0] = False

            return 1 + max(l,r) # need to return the height max height here to use in our recursion
          
        dfs(root)    
        return ans[0]
    
