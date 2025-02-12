class Solution(object):
    def productExceptSelf(self, nums):

        answer = [1] * len(nums)
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * right
            right *= nums[i]
        return answer