class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0

        # this is essentially doing list 
        # popping and appending but with bits instead
        # we are pusing the bits from the end of
        # n to the start of res therefore reversing it
        # loop 32 (because we have 32 bit integer)

        for i in range(32):
            # shift bits left
            # returns res with bits shifted left by 1
            res = res << 1
            # this gets the last bit(far right) of n 
            #(same as n%2 on an int 46 would give us 6)
            bit = n & 1 
            
            # add bit to result
            res += bit
            # shift bits of n to the right by 1 so we can get the next bit to add to our result
            n = n >>1
            print (bin(res), bin(n))
            
            

        return res
