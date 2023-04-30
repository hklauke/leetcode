class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        checked = []
        # keep looping until n == 1 and then return true
        while n != 1:
            # pythonic for loop to build sum number
            n = sum([int(i) ** 2 for i in str(n)])
            # if we've already seen that number then we've discovered our cycle
            # and n will  never equal 1
            if n in checked:
                return False
            else:
                checked.append(n)
        else:
            return True
