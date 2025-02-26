class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums))
        dp[0] = nums[0] # 2
        dp[1] = max(nums[0], nums[1])

        for n in range(2, len(nums)):
            dp[n] = max(dp[n-1], dp[n-2] + nums[n])

        return dp[-1]
        '''
        dp[2] 0번 집을 털었으면 2번 집 털 수 있고, 1번 집 털었으면 지금 못 털음
        dp[2] = max(dp[1], dp[0]+nums[2]) # 11
        dp[3] 0번 집 털었고 2번집 털었으면 3번집 못 털고, 1번 집 털었으면 3번집 털 수 있음.
        dp[3] = max(dp[2], dp[1] + nums[3]) # 11, 10
        dp[4] 0번 집 털었고 2번집 털었으면 4번 집 털 수 있고, 1번 집 털고 3번집 털었으면 지금 4번집 털 수 없음.
        dp[4] = max(dp[3], dp[2] + nums[4])
        '''