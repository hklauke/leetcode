class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # build a dict of values and the number of times they appear
        hashmap = {}
        for i in nums:
            if hashmap.get(i):
                hashmap[i] +=1
            else:
                hashmap[i] = 1

        result = []
    
        # find largest value and loop through hashmap. change max values to
        # 0 and then go again
        while len(result) < k:
            nmax=max(hashmap.values())
            for i in hashmap.keys():
                if hashmap[i] == nmax:
                    result.append(i)
                    hashmap[i] = 0    
        return result
