class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # initally have our input array
        # start with first index, get all permutations of rrest of the indicies
        # keep going until get single index, this is base case
        # then backtrack and add other permutations to result

        res = []

        # Base CASE
        if len(nums) == 1:
            # just returrn itself as a list
            return [nums[:]]
        
        for i in range(len(nums)):
            # need to exlude the number we are working against
            n = nums.pop(0)
            # recusrive call to get a list of said numbers
            perms = self.permute(nums)

            ## THIS IS THE IMPORTANT BIT
            # we're taking the output of this perms and appending the number we popped
            # so if we have [1,2]
            # our perms our 1,2 and 2,1 because we pop 1 and then loop through the remainder
            # and append the number we popped. aka pop 1, return 2, append 1 = [2,1] and then
            # pop 2, return 1, append 2 and [1,2]
            for i in perms:
                i.append(n)
            # add our permutations to the result
            res.extend(perms)
            # re add our number back to cleanup
            nums.append(n)

        return res
