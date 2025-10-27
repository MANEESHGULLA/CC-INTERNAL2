#meeting room 1

def maxMeetings(start,end):
  meetings=sorted(zip(start,end),key=lambda x:x[1])
  curr_time=-1
  time_slot=[]

  for s,e in meetings:
    if s>curr_time:
      time_slot.append((s,e))
      curr_time=e

  return time_slot

Start = [1, 4,6,8]
End = [3,5,9,10]
print(maxMeetings(Start, End)) #[(1, 3), (4, 5), (6, 9)]
