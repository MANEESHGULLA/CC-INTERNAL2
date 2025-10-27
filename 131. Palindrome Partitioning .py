#palindrome partiitoning
def partition(s):
    result=[]

    def palindrome(sub):
        return sub==sub[::-1]

    def backtrack(start,path):
        if start==len(s):
            result.append(list(path))

        for end in range(start+1,len(s)+1):
            sub=s[start:end]

            if palindrome(sub):
                path.append(sub)
                backtrack(end,path)
                path.pop()
    backtrack(0,[])

    return result
  
print(partition("aabb"))

