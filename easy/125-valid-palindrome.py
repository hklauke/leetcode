class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
            
        l = 0
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l = l+1
                continue
            if not s[r].isalnum():
                r = r-1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True


    # Nice two pointer solution
    # i had originally done this by creating a new string without
    # excess characters and uppercase and then used [::-1] but this
    # is a more algorithmic solve
