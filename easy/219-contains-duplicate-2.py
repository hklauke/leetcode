class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hmap ={}
        # return True if 2 distinct indicies that are equal and the abs value of the diff < k
        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = i
            else:
                if abs(i-hmap[nums[i]]) <= k:
                    return True
                else:
                    hmap[nums[i]] = i

        return False

