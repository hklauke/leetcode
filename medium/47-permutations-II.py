class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        if len(nums) == 1:
            # nums[:] is a pythonic way to make a copy
            return [nums[:]]
          
        # similiar solution to perms one except we want to avoid duplicates
        # so we include a "checked" array to keep track of the lists we've already done
        checked = []
        for i in range(len(nums)):
            n = nums.pop(0)
            if n not in checked:
                new = self.permuteUnique(nums)
                for i in new:
                    i.append(n)
                res.extend(new)
            checked.append(n)
            nums.append(n)
        print(checked)
        return res
      
      # example of output of checked
      # nums = [1,1,2]
      
      # [1, 2]
      # [1, 1]
      # [1, 1, 2]
      
      # we're going to run into the same situations as we backtrack through the list so 
      # keeping track of the situations we've already run into makes this simple and we can ignore them
