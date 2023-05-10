class Solution(object):
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # We're going to loop through each row of the matrix but since this
        # matrix is sorted we can just check the last element and see if our
        # target value will be in that row or not, we're doing partial binary
        # search here so not entirely optimal.
        for i in range(len(matrix)):
            if matrix[i][r] < target:
                continue
            l= 0
            r = len(matrix[0]) -1
            while l <= r:
                mid = (l+r) //2
                if target == matrix[i][mid]:
                    return True
                elif matrix[i][mid] < target:
                    l = mid +1 
                elif  matrix[i][mid] > target :
                    r = mid -1
            
        return False

    # the other option here is to perform binary search twice
    # once to find the correct row, once to find the number in the row
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        bot = 0
        top = len(matrix) -1
        while bot <= top:
            row = (bot + top) //2
            if matrix[row][0] > target:
                top = row - 1 
            elif matrix[row][-1] < target:
                bot = row + 1
            else:
                break
        l= 0
        r = len(matrix[0]) -1
        while l <= r:
            mid = (l+r) //2
            if target == matrix[row][mid]:
                return True
            elif matrix[row][mid] < target:
                l = mid +1 
            elif  matrix[row][mid] > target :
                r = mid -1
            
        return False
