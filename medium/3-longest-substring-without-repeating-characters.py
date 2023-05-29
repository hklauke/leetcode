class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # USed a sliding window algorithm
        longest =  []
        curr_long = 0
        j =0
        while j < len(s):
            if s[j] not in longest:
                longest.append(s[j])
                j+=1
            else:
                longest.pop(0)
            
            if len(longest) > curr_long:
                curr_long = len(longest)

        return curr_long
