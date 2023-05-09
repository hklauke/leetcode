# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # preorder traversal order is 
        # visit root
        # visit left
        # visit right
        ans = []
        def helper(root):
            if root == None:
                return 
            ans.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return ans
