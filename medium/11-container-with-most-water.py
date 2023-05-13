class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) -1
        # this was a 2 pointer problem but just calculating total area (volume) 

        volume = 0 # volume = height * number of rows
        while l < r:
            
            curr_vol = min(height[l], height[r]) * (r - l)
            
            if volume < curr_vol:
                volume = curr_vol
      
            if height[l] < height[r]:
                l = l +1
            else:
                r = r -1
            
        return volume
