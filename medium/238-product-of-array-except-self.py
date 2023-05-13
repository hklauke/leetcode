class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # speed optimization
        res = [1] * len(nums)
        suffix = []
        pre, post = 1, 1
        # create our suffixes here, multiplying each time
        for i in range(len(nums)-1, -1, -1):
           suffix.append(post)
           post = post* nums[i]

        
        # finding our prefixes and multiplying them by the suffix
        # and then storing in result array
        for i in range(0, len(nums)):        
           res[i] = (pre * suffix[len(nums)-i-1])
           pre = pre*nums[i] 
        
        return res
        
