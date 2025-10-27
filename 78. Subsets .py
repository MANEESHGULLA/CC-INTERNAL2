# subset1
def subsets(nums):
    result = []

    def backtrack(idx, curr_subset):
        result.append(list(curr_subset))

        for i in range(idx, len(nums)):
            curr_subset.append(nums[i])
            backtrack(i + 1, curr_subset)
            curr_subset.pop()

    backtrack(0, [])
    return result


# ✅ Example Inputs
print(subsets([1, 2, 3])) #[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


