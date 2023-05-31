class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i=i+1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j+=1
        res.extend(nums1[i:])
        res.extend(nums2[j:])
        
        
        if len(res) % 2 ==0:
            mid = len(res) // 2
            return (float(res[mid] + res[mid-1])/2)
        else:
            mid = (len(res) -1) //2
            return res[mid]

