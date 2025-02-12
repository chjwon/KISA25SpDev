class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)

        # Multiply 0 to i-1 elements and store it in i
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        # Multiply i+1 to n-1 elements and multiply it with the previous i
        suffix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
