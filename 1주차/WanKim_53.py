class Solution(object):
    def maxSubArray(self, nums):

        n = len(nums)

        result = [0]*n
        m = result[0] = nums[0]
        tmp = 0

        for i in range(1, n):
            if result[i-1]<0:
                tmp = 0
            else: 
                tmp = result[i-1]

            result[i] = nums[i]+tmp
            m = max(m,result[i])

        return m
        """
        :type nums: List[int]
        :rtype: int
        """
        