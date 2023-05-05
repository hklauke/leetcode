class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # strip removes all leading and trailing spaces from a string
        # split separates a string based on the input
        slist = (s.strip()).split(" ")
        return len(slist[-1])
