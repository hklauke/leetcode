class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        # only need to check first string. if they all have the same prefix it
        # doesn't matter how long this one is
        for i in range(len(strs[0])):
            # loop through strings and check if we've gotten to the end of any
            # of our strings or if the str characters don't match the first
            # string
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                # if either of these two cases match then we've found the end
                # of our prefix
                   return result
            # otherwise prefix is still good and keep adding to it
            result = result + strs[0][i]   
                
        return result    
                    
                    
