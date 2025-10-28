#no of provinces
def numberOfProvinces(graph):
  provinces=0
  n=len(graph)
  visited=[0]*n

  def dfs(i):
    for j in range(n):
      if graph[i][j]==1 and not visited[j]:
        visited[j]=1
        dfs(j)


  for i in range(n):
    if not visited[i]:
      visited[i]=1
      provinces+=1
      dfs(i)

  return provinces

graph=[[1,1,0,0,0,0],[1,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,1]] #3
print(numberOfProvinces(graph))
