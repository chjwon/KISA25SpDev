import math

class Solution(object):
    def uniquePaths(self, m, n):
        #궁금한 점.. 실제 코테에서 모듈 import해서 사용해도 무방한가
        result = math.factorial(m+n-2) / (math.factorial(m-1) * (math.factorial(n-1)))
        return result