def combinationSum(candidates, target):
    result = []

    def backtrack(idx, path, curr_sum):
        if curr_sum == target:
            result.append(list(path))
            return

        if curr_sum > target:
            return

        for i in range(idx, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, curr_sum + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return result


print(combinationSum([2,3,6,7], 7)) #[[2, 2, 3], [7]]
print(combinationSum([2,3,5], 8)) #[[2, 2, 2, 2], [2, 3, 3], [3, 5]]

