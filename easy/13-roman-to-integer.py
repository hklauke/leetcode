class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        r_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        for i in range(len(s)-1):
            # if the value is less than the value of the next subtract otherwise add
            # this is becasue 10 < 100 we subtract 10 but then add 100 which gives us 90 which
            # is the value of the numbeer we wanted anyway
            if r_value[s[i]] < r_value[s[i+1]]:
                sum = sum - r_value[s[i]]
            else:
                sum = sum + r_value[s[i]]
        # have to add the last value as well because we're missing that in the loop so we don't
        # have index out of bounds
        return sum + r_value[s[-1]]
