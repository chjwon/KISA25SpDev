class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            for j in range(i+1,n):
                for k in range(j+1,n):
                    tmp = 0-nums[i]-nums[j]
                    if nums[k] > tmp: break
                    if tmp == nums[k] and [nums[i],nums[j],nums[k]] not in result:
                        result.append([nums[i],nums[j],nums[k]])
        return result
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
# Time Limit Exceeded