class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        # tri
        tri = []
        for i in range(1,numRows +1):
            row = []
            for j in range(i):
                if j == 0 or j == i-1:
                    row.append(1)
                else:
                    row.append(tri[i-2][j-1]+tri[i-2][j])
            tri.append(row)
        return tri
