class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # we're using the number in the array as the index and changing the number at that index to a negative number. 
        # If there are missing numbers then those indices won't be negative because that value is missing from the array
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            
            nums[index] = abs(nums[index]) * -1


        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
