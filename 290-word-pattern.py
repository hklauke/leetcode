class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
   
        bhash={}
        arr = s.split(' ')

        if len(arr) != len(pattern):
            return False

        if len(set(arr)) != len(set(pattern)): 
            return False # for the case w = ['dog', 'cat'] and p = 'aa'

        for i in range(len(pattern)):
            if bhash.get(pattern[i]) == None:
                bhash[pattern[i]] = arr[i]
            else:
                if arr[i] != bhash[pattern[i]]:
                    return False

        return True
