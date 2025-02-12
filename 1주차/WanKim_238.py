class Solution(object):
    def productExceptSelf(self, nums):

        result = [1]*len(nums)

        pre = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]
        
        post = 1
        for j in range(len(nums)-1, -1, -1):
            result[j]*=post
            post *= nums[j]
        
        return result
        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        