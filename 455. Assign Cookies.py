def assignCookies(students,cookies):
  students.sort()
  cookies.sort()
  satisfied=0
  i=j=0

  while i<len(students) and j<len(cookies):
    if cookies[j]>=students[i]:
      satisfied+=1
      i+=1
      j+=1
    else:
      j+=1

  return satisfied

students = [1, 2, 3,4]
cookies = [1, 2,2,3]
print(assignCookies(students, cookies)) #3
