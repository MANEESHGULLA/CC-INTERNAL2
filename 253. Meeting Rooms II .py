#meeting room2

def minMeetingRooms(intervals):

  start=sorted([i[0] for i in intervals])
  end=sorted([i[1] for i in intervals])

  rooms=1
  max_rooms=1
  i=1
  j=0

  n=len(intervals)

  while i<n:
    if start[i]<end[j]:
      rooms+=1
      i+=1
    else:
      rooms-=1
      j+=1

    max_rooms=max(rooms,max_rooms)

  return max_rooms

intervals = [[0,30],[5,10],[15,20]]
print(minMeetingRooms(intervals)) #2
