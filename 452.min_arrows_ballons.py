def minArrows(points):
  points.sort(key=lambda x:x[1])
  arrows=1
  current_end=points[0][1]

  for x_start,x_end in points[1:]:
    if x_start>current_end:
      arrows+=1
      current_end=x_end

  return arrows

points = [[10,16],[2,8],[1,6],[7,12]]
print(minArrows(points)) #2
