def orangesRotting( grid):
    q=[]
    fresh=0
    rows=len(grid)
    cols=len(grid[0])
    time=0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==1:
                fresh+=1
            elif grid[i][j]==2:
                q.append([i,j])


    directions=[[0,1],[0,-1],[1,0],[-1,0]]

    while q and fresh>0:

        for i in range(len(q)):
            r,c=q.pop(0)
            
            for dr,dc in directions:
                row= dr+r   
                col=dc+c

                if row<0 or row>=rows or col<0 or col>=cols or grid[row][col]!=1:
                    continue
                
                grid[row][col]=2
                fresh-=1
                q.append([row,col])
        
        time+=1
    
    return time if fresh==0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid)) #4
