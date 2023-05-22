## Binary Search
- **Whenever we encounter a sorted Array , List , or Matrix in a coding problem and we are asked to find a specific number**, we all know that the best algorithm we can use is the binary search.
- The time complexity of binary search **O(log n)**. it requires the input array to be sorted
- Given an array we find the ends (0,length) and find a middle number (L+R) //2 and then run comparison, changing the search params as we compare items in an array. 
```
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
```

