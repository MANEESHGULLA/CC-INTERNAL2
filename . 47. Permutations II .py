#permutation 2
def permuteUnique(nums):
    nums.sort()
    result=[]

    def backtrack(idx):
        if idx==len(nums) and nums not in result:
            result.append(list(nums))

        for i in range(idx,len(nums)):
            nums[i],nums[idx]=nums[idx],nums[i]
            backtrack(idx+1)
            nums[i],nums[idx]=nums[idx],nums[i]

    backtrack(0)
    return result

print(permuteUnique([1,1,2])) #[[1, 1, 2], [1, 2, 1], [2, 1, 1]]




