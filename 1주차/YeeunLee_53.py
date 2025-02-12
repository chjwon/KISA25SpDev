class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = max_sum = tem_start = 0
        
        for i, num in enumerate(nums):
            if i == 0: 
                cur_num = max_num = nums[i]

            else:
                if cur_num + num < num:
                    cur_num = num
                    tem_start = i

                else:
                    cur_num = cur_num + num
                
                if cur_num > max_num:
                    max_num = cur_num

        return max_num

                
