class Solution(object):
    def climbStairs(self, n):
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2
        
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[-1]



        '''
        n == 0 return 0
        n == 1 return 1
        n == 2 return 1 + 1
        n == 3 return 3가지 n == 2 + 1
        111, 12, 21

        n == 4 return 5 ( n == 3 + 2 )
        1111 112 121 211 22
        
        n == 5 return 8 ( n == 4 + 3)
        11111 1112 1121 1211 2111 122 212 221 

        n == i return n == i - 1 + n == i - 2

        dp bottom_up
        '''