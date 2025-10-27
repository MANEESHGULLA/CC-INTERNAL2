class Node:
  def __init__(self,val=0,neighbors=None):
    self.val=val
    self.neighbors=neighbors if neighbors is not None else []

class Solution:
  def cloneGraph(self,node):

    oldToNew={}

    def dfs(node):
      if node in oldToNew:
        return oldToNew[node]

      copy=Node(node.val)
      oldToNew[node]=copy

      for nei in node.neighbors:
        copy.neighbors.append(dfs(nei))
      
      return copy
  
    return dfs(node) if node else None
  
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

s1=Solution()
cloned=s1.cloneGraph(n1)

def printGraph(node,visited=set()):

  if node in visited:
    return
  
  visited.add(node)

  print(f"node {node.val} -> {[n.val for n in node.neighbors ]}")

  for nei in node.neighbors:
    printGraph(nei,visited)

print("Original Graph:")
printGraph(n1)

print("\nCloned Graph:")
printGraph(cloned)

