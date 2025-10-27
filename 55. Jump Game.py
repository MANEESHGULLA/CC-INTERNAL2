def canJump(nums):
    max_reach = 0
    n = len(nums)

    for i in range(n):
        if i > max_reach:
            return False  # can't reach this index
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= n - 1:
            return True  # can reach or go beyond last index

    return True

# Examples
print(canJump([2,3,1,1,4]))  # Output: True
print(canJump([3,2,1,0,4]))  # Output: False
