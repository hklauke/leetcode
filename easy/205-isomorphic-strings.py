class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        #BUILD 2 hashmaps and creating a mapping for each letter to the other string
        # if there are any duplicates we return false
        # have to do this both ways because one letter cannot map to more than one other letter
        # f -> b
        # o -> a
        # o -> r
        # this is false but if we did it the other way
        # b -> f
        # a -> o
        # r -> o
        # This is also false but would't fail if we didn't do the foo side as well. 
        
        
        char_map = {}
        char2_map = {}

        for i in range(0,len(s)):
                 
            if s[i] not in char_map:
                char_map[s[i]] = t[i]
            elif char_map[s[i]] != t[i]:
                return False
            
            if t[i] not in char2_map:
                char2_map[t[i]] = s[i]
            elif char2_map[t[i]] != s[i]:
                return False
            

        return True
