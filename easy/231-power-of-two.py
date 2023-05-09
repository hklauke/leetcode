class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # here we basically say that if n can be divided by 2 and our recursive
        # call serves 2 until n ==1 and then return True
        if n == 0: 
            return False

        if n%2 == 0 and self.isPowerOfTwo(n //2):
            return True
        if n==1:
            return True

        return False

# Same solution but using a while loop instead
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: 
            return False

        while n != 1:
            if n % 2 == 0:
                n = n //2                
            else:
                return False
        
        return True
