# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        count = 0
        stack = []
        # We're going to keep a counter of the current level we are on.
        # Everytime we iterate and get to another level we keep a record of
        # that level and add to an array in the corresponding location
        def levelorder(root,count):
            if root == None:
                return
            if count == 0:
                stack.append([root.val])
            else:
                # need to make sure that the actual location exists before
                # adding to it
                if len(stack) == count:
                    stack.append([root.val])
                else:
                    stack[count].append(root.val)

            levelorder(root.left, count+1)
            levelorder(root.right,count+1)

        levelorder(root, count)
        return stack
        
