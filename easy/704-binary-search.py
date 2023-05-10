class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l = 0
        r = len(nums) -1
       # Divide list in half to get middle number, find mid again, if the value
       # at mid is less than target move left pointer to mid +1
       # if mid value greater than target, move right pointer to mid +1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid +1
            else:
                r = mid-1
        return -1
