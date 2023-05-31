class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        k = 0
        flowerbed.insert(0,0)
        flowerbed.append(0)

        for i in xrange(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    k+=1

        return(k >= n)
