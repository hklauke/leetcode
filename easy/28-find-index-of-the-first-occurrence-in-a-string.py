class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        # we're just looking for the first character to match and then taking
        # a slice. This isn't the most efficient way to do this since python
        # makes a copy of the array when performing slice operations but it's
        # simpler than nested for loops                
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i

        return -1
