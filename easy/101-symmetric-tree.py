# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False

        left,right = [root.val], [root.val]
        # Basically i built a recursive function here to just build two lists
        # and compare the values after
        # we have to traverse the opposite direction in order to build the same
        # list if the child nodes are actually symmetric.
        def traverse(root,stack, dirr):
            if root == None:
                stack.append(None)
                return
            stack.append(root.val)
            if dirr == "left":
                traverse(root.left, stack, dirr)
                traverse(root.right, stack, dirr)
            elif dirr == "right":
                traverse(root.right, stack, dirr)
                traverse(root.left, stack, dirr)

        traverse(root.left, left, "left")
        traverse(root.right, right, "right")


        if left == right:
            return True
        return False

