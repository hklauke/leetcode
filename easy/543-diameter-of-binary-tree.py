# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        longest = [0]

        def dfs(node):
            if not node:
                return -1 # height of tree if no node
            
            left = dfs(node.left) # height of left tree
            right = dfs(node.right) # height of right tree

            # diameter of tree is height of left + height of right
            # plus 1 plus 2 becasue for each tree there is an edge going to it we need to return -1 to offset adding our edge
            if longest[0] < (2+left+right):
                longest[0] = 2+left+right

            return 1 + max(left, right)


        dfs(root)

        return longest[0]


        
