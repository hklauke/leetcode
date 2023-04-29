class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        # essentially taking what we learned from reverse bit
        # and applying it, pop last bit, shift right. Since it's all 1's
        # and 0's anyway we just add the bits to count and don't need 
        # conditionals
        for i in range(32):
            bit = n &1
            count +=bit
            n = n >> 1
        return count
