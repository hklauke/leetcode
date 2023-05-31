class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        
    # split list in 2  recursively, until individual values
    # this is the divide step

    # MERGE SORT
        if len(nums) == 1:
            return nums
        
        mid = len(nums) //2
        left = self.sortArray(nums[:mid])    
        right = self.sortArray(nums[mid:])
        merged = [] 
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i +=1
            else:
                merged.append(right[j])
                j+=1
        
        merged += left[i:]
        merged += right[j:]
        return merged
