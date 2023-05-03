class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        # Idea here is to create a hashmap with the number of times a value shows up in the longer list
        # and then go through the shorter list and check those values against the hash
        # in order to only add the values the corrrect number of times we subtract the count so if the value shows up again in
        # shorter but wasn't in longer then we won't include it in the ans
        if len(nums1) < len(nums2):
            shorter = nums1
            longer = nums2
        else: 
            shorter = nums2
            longer = nums1

        hashmap = {}
        for i in longer:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        
        ans = []

        for i in shorter:
            if i in hashmap and hashmap[i] != 0:
                ans.append(i)
                hashmap[i] -= 1
        
            
        return ans
