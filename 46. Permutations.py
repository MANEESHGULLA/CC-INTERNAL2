def permute(nums):
    result = []

    def backtrack(idx):
        if idx == len(nums):
            result.append(list(nums))
            return

        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            backtrack(idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]

    backtrack(0)
    return result


# ✅ Example Inputs
print(permute([1, 2, 3])) #[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
