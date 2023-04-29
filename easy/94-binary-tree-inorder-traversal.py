# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # go left, visit root, go right
        # traverse the tree going left and print it's value,
        # then print the the root value
        # finally go right return right value
        stack = []
        def inorder(root):
            if root == None:
                return

            #Doesnt' need to be a return since we're editing a global variable. Will run through every case with right and left on each node
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
        inorder(root)
        return stack
