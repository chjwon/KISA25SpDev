def maxSubArray(nums):
    max_sum = nums[0]

    for start in range(len(nums)):
        current_sum = 0
        for step in range(start, len(nums)):
            current_sum += nums[step]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum
