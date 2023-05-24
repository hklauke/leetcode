# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

       # dfs with a max value changing, pretty straightforward. I used a queue
       # here for faster append operations
        ans = deque([])
        def dfs(node, base):
            if node is None:
                return
            
            if node.val >= base:
                ans.append(node.val)
                base = node.val
            
            dfs(node.left, base)  
            dfs(node.right, base) 

        dfs(root, root.val)

        return len(ans)
