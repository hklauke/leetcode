class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        longest = ""
        ans = ""
        # consider each letter the middle
        # work our way out and look for equal characters on each side of the single character
        # when no longer a palindrome then iterate
        if len(s) < 2:
            return s

        def isPalindrome(l,r, longest):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) + 1> len(longest):
                    longest = s[l:r+1]
                l -=1
                r +=1
            return longest

        for i in range(len(s)):
            l,r  = i,i,
            # making sure our pointers are in bound and have equal value
            # we have to run it twice to check for odd length strings and even lengthstrings
            odd = isPalindrome(l,r, longest)
            if len(odd) > len(ans):
                ans = odd
            # 
            l,r, = i,i+1
            even = isPalindrome(l,r, longest)
            if len(even) > len(ans):
                ans = even
        return ans
