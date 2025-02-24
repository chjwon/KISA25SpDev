class Solution(object):
    def climbStairs(self, n):
    
        dp = [1,1,2] #initial
        
        for i in range(3, n + 1):
            dp.append(dp[i-1] + dp[i-2])
        
        #print(dp)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else: 
            return dp[-1]
        