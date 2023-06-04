def find_duplicate(nums):
    #if not nums:
    #    return False
    #if not isinstance(nums, int):
    #    return False
    #if len(nums) < 2:
    #    return False
    #if any(num <= 0 for num in nums):
    #    return False
    #nums.sort()
    #for i in range(1, len(nums)):
    #    if nums[i] == nums[i - 1]:
    #        return nums[i]
    #return False

    if (not nums or any(not isinstance(num, int) for num in nums)
        or len(nums) < 2 or any(num <= 0 for num in nums)):
        return False

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

    return False
