class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # The trick here is to start at the end of the array and work our way
        # to the beginning
        curMax = -1
        for i in range(len(arr)-1, -1, -1):
            temp = arr[i] 
            arr[i] = curMax
            if temp > curMax:
                curMax = temp
            
        return arr       
