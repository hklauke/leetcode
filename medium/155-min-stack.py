class MinStack(object):
    # This was a weird quesiton because of the wording but we essentially just
    # reimplement a stack using default python functions and we keep 2 stack's
    # around, where one is our object but the other just contains our miniumu
    # numbers at the end of the array
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minStack:
            val = min(val, self.minStack[-1])
        self.minStack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]
        else: 
            return 0

