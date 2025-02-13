class Solution(object):
    def maxSubArray(self, nums):
        list_int = []
        list_i = []
        for i in range(0, len(nums)):
            
            list_i.append(nums[i])
            temp = nums[i]

            for j in range(i + 1, len(nums)):
                nxt = temp + nums[j]
                list_i.append(nxt)
                temp = nxt

            list_int.append(max(list_i))

        return(max(list_int))
