class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cnt = 0
        ff = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ff+=1
        while ff > 0:
            flag = False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 2:
                        if i+1 < len(grid) and grid[i+1][j] == 1:
                            grid[i+1][j] = 3
                            ff-=1
                            flag = True
                        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                            grid[i][j+1] = 3
                            ff-=1
                            flag = True
                        if i-1 >=0 and grid[i-1][j] == 1:
                            grid[i-1][j] = 3
                            ff-=1
                            flag = True
                        if j-1>=0 and grid[i][j-1] == 1:
                            grid[i][j-1] = 3
                            ff-=1
                            flag = True
            if not flag:
                return -1 
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
            cnt+=1
        return cnt
            
            

                    