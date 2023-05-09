class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check board row
        rmap ={}
        cmap = {}
        grid = {}
        for row in range(0, 9): 
            for col in range(0, 9):
                if board[row][col] == '.':
                    continue
                # Build col hashmap
                if board[row][col] in cmap:
                    if col in cmap[board[row][col]]:    
                        return False
                    else:
                        cmap[board[row][col]].append(col)
                else:
                    cmap[board[row][col]] = [col]

                # build row hashmap
                if board[row][col] in rmap:
                    if row in rmap[board[row][col]]: 
                        return False

                    else:
                        rmap[board[row][col]].append(row)
                else:
                    rmap[board[row][col]] = [row]
                

                 # check 3x3 and build grid
                g1  = row/3 
                g2 = col/3
                if board[row][col] in grid:
                   
                    if [g1,g2] in grid[board[row][col]]:
                        return False
                    else:
                        grid[board[row][col]].append([g1,g2])
                else:
                    grid[board[row][col]] = [[g1,g2]]

        return True
       
## This took some thinking but essentially we're building 2 dicts where each dict is a row or column and makingsure the number doesn't exist in said row or column. 
# for the 3x3 we use integer division by 3 to isolate a block (8/3 = 2) which is the bottom right block which if we're thining about a matrix would be position (2,2)
# in the grid and then add the position for that specific number. It's the inverse data setup for what we are doing for rows and cols
