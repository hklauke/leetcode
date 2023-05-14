class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # so here we need to use binary search to 
        # find the  minium number, BUT the array has
        # been rotated and a Binary search needs to 
        # run on a sorted array. 
        # the trick here is to figure out how to sort the array 
        # or figure out where to start the search 

        # maybe we can find mid and then compare the numbers around it? 
        # that wouldn't work in this scenario [4,5,6,7,3] 
        # maybe we can look at the first and last element and compare their values?
        # if last < first we can work from the back
        # if last > first we can work from the front

        l = 0
        r = len(nums) -1
        
        #find the mid and compare it to the right, if it's 'less we don't have 
        #to worry about whatever is next to it and start looking at the left side of the array'
        lowest = 0
        while l < r:
            mid = (l+r) //2
        
            if nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid +1
            
        return nums[l]
