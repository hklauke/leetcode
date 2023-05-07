 #RECURSION
        if root == None:
            return 0 
        # calls itself to continue finding max depth of tree 
        # and in context of root will always return the max depth in 
        # it's context to higher up
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
