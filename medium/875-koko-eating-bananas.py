class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 0, max(piles)
        while l + 1 < r:
            k = (l + r)//2
            hours = 0
            for i in piles:
                hours += ceil(i/k)
            
            if hours > h:
                l = k
            
            else:
                r = k
                
        return r
