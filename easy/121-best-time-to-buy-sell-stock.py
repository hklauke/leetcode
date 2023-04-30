class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # find greatest difference between 2 elements in array with the smaller number being first in the array and the larger number being second
        cheapest = prices[0]
        profit = 0
        for i in prices:
            # is this price cheaper than we've seen before?
            if i > cheapest:
            # if i subtract current by cheapest is the profit higher than before
                if i - cheapest > profit:
                    profit = i-cheapest
            else: 
                cheapest = i

        return profit

            
