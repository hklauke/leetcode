# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepthRecursion(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        #RECURSION
        if root == None:
            return 0 
        # calls itself to continue finding max depth of tree 
        # and in context of root will always return the max depth in 
        # it's context to higher up
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    def maxDepthBFS(self, root):
        #BFS - (Breadth first search)
        # Typically invovles a queue
        if not root:
            return 0
        
        level =0 
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            level +=1
        return level
    
    # IDPFS (Iterative Depth First Search)
    def maxDepth(self, root):
        res = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()

            if node:
                res = max(res, depth)
                stack.append([node.left, depth +1])
                stack.append([node.right, depth +1])
        return res
 
