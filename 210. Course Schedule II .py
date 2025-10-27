
def findOrder(numCourses, prerequisites):
    preMap={i:[] for i in range(numCourses)}

    for crs,pre in prerequisites:
        preMap[crs].append(pre)
    
    visited=set()
    cycle=set()
    output=[]

    def dfs(crs):
        if crs in cycle:
            return []
        
        if crs in visited:
            return True
        
        cycle.add(crs)

        for pre in preMap[crs]:
            if not dfs(pre): return False
        
        visited.add(crs)
        cycle.remove(crs)
        output.append(crs)
        return True
    
    for crs in range(numCourses):
        if dfs(crs)==False:
            return []
    
    return output

numCourses = 2
prerequisites = [[1,0]]
print(findOrder(numCourses,prerequisites)) #[0,1]

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(numCourses,prerequisites)) #[0,2,1,3]

    
