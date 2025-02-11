class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = [0 for i in range(len(nums))]
        answer[0] = nums[0]
        cur_sum = nums[0]
    
        for index, value in enumerate(nums):
            if index == 0:
                continue
            if cur_sum < value:
                cur_sum = max(value, cur_sum + value)
            else:
                cur_sum += value

            answer[index] = max(cur_sum, answer[index - 1])

            #print(index,"answer[i] = " , answer[index],"cur_sum = ", cur_sum)
        return answer[len(nums)-1]