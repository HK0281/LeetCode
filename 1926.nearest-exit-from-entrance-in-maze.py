#
# @lc app=leetcode id=1926 lang=python3
#
# [1926] Nearest Exit from Entrance in Maze
#

# @lc code=start
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        def isValid(row, col):
            return 0<=row<m and 0<=col<n and maze[row][col]=='.'
        x=entrance[0]
        y=entrance[1]
        seen = {(x,y)}
        queue = deque([(x,y,0)])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        steps = 0

        while queue:
            row,col,steps = queue.popleft()
            if (row,col)!=(x,y) and (row==0 or col==0 or row==m-1 or col==n-1):
                return steps
            for dx, dy in directions:
                nextrow,nextcol=row+dx,col+dy
                if isValid(nextrow,nextcol) and (nextrow,nextcol) not in seen:
                    seen.add((nextrow,nextcol))
                    queue.append((nextrow,nextcol,steps+1))
        
        return -1
# @lc code=end

