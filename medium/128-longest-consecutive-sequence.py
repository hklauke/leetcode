class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        # REally creative solution that I did not come up with but genius
        # So if a number is the start of a sequence then 1- that number wont
        # exist in the array (we can use a set since we dont' care about
        # duplicates)
        # then we loop through the array as long as that set still contains the next
        # number and continue to increase our counter. Then compare counters
        # and return
        for i in numSet:
            if i-1 not in numSet:
                count = 1
                while (count+i) in numSet:
                    count = count+1
                if count > longest:
                    longest = count

        return longest
