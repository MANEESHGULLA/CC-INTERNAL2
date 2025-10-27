#wordbreak
def wordBreak(s, wordDict):
    n=len(s)
    dp=[False]*(n+1)
    dp[n]=True
    for i in range(len(s)-1,-1,-1):
        for w in wordDict:
            if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                dp[i]=dp[i+len(w)]
            if dp[i]:
                break

    return dp[0]

s="leetcode"
wordDict=['leet','code']
print(wordBreak(s,wordDict))

