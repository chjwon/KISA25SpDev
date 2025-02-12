class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        answer = []
        
        for i in range(1, len(nums)):
            left.append(left[i-1] * nums[i-1])

        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            answer.append(left[i] * right[i])
        
        return answer
