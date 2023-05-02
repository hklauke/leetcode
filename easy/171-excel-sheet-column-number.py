class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # I actually quite liked this problem
        # basically we create a hashmap and assign each letter of the alphabet
        # a value. When we look at a column we need to consider that for each
        # addition letter we add (AB, AAB, AAAB) we've got to multiply the
        # value 26 ^(number of rows) because once we've added a new column
        # we've gone through the entire alphabet again.
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        hashmap = {}
        for i in range(0,26):
            hashmap[alph[i]] = i +1
        
        sum = 0
        length = len(columnTitle)
        for i in range(0, length-1):
            
            sum += hashmap[columnTitle[i]] * (26 ** (length-1-i))

        sum +=hashmap[columnTitle[length-1]]
        
        return sum
        
