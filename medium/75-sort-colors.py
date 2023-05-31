class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        # choose the rightmost element as pivot
        r = len(nums) -1
        l = 0
        zero = 0
        
        while (l <= r):
            if nums[l] == 0:
                nums[l], nums[zero] = nums[zero], nums[l]
                l=l+1
                zero=zero+1
            elif nums[l] ==2:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
            else:
                l+=1


