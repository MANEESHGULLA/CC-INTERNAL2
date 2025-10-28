def maxArea(grid):
  rows=len(grid)
  cols=len(grid[0])
  visited=set()


  def dfs(r,c):
    if r<0 or r==rows or c<0 or c==cols or grid[r][c]==0 or (r,c) in visited:
      return 0
    
    visited.add((r,c))

    return (1+ dfs(r+1,c)+
                dfs(r-1,c)+
                dfs(r,c+1)+
                dfs(r,c-1))
  
  area=0
  for i in range(rows):
    for j in range(cols):
      area=max(area,dfs(i,j))
  
  return area

grids=[[0,0,1,0,0,0,1],[0,0,0,0,1,1,1],[0,0,1,1,0,0,0],[0,0,1,1,1,0,0]]
print(maxArea(grids))
