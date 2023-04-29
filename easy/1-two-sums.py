class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            alt_num = target - nums[i]
            if (alt_num) in hashmap:
                return [i, hashmap[alt_num]]
            hashmap[nums[i]] = i
            
