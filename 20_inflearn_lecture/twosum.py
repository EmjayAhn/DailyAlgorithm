def twoSum(nums, target):
    nums.sort()
    
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] == target:
            return [l, r]
    return False

print(twoSum(nums=[3, 2, 4], target = 6))
    
