class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        # This one is pretty straightforward. just santize the string according to the rules and add it to thee list
        arr = []
        for i in emails:
            temp = i.split("@")
            temp[0] = temp[0].replace('.', '').split("+")[0]
            
            temp = "@".join(temp)
            if temp not in arr:
                arr.append(temp)
        print(arr)
        return len(arr)
