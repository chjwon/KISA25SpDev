class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        currentMax, globalMax = nums[0], nums[0]
        for i in range(1, len(nums)):
            currentMax = max(nums[i], currentMax + nums[i])
            globalMax = max(globalMax, currentMax)

        return globalMax
