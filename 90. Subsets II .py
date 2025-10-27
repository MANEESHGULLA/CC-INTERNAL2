#subset2
def subsetsWithDup(nums):
    nums.sort()
    result=[]

    def backtrack(idx,curr_subset):
        if curr_subset not in result:
            result.append(list(curr_subset))

        for i in range(idx,len(nums)):
            curr_subset.append(nums[i])
            backtrack(i+1,curr_subset)
            curr_subset.pop()

    backtrack(0,[])
    return result
print(subsetsWithDup([1,2,2])) #[[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
