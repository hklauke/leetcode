# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        queue = deque([root])
        # bfs search with a recursive dfs to find matching subtree
        def isMatch(q,p):
            if q == None and p == None:
                return True
            if q and p and q.val == p.val:
                return isMatch(q.left, p.left) and isMatch(q.right, p.right)

        while len(queue) > 0:
            for i in range(len(queue)):
                node = queue.popleft()
                    
                if node.val == subRoot.val:
                    if isMatch(node, subRoot):
                        return True
                        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return False

