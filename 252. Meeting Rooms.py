#meeting rooms

def meetings(intervals):
  start=sorted([i[0] for i in intervals] )
  end=sorted([i[1] for i in intervals] )

  for i in range(1,len(start)):
    if start[i]<end[i-1]:
      return False
    
  return True
      
    
intervals=[[1,3],[2,5],[6,8]]
print(meetings(intervals)) #False
  
