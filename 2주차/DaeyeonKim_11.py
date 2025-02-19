class Solution(object):
    def maxArea(self, height):
        p1 = 0
        p2 = len(height) - 1
        answer = min(height[p1], height[p2]) * (p2 - p1)
        while p1 <= p2:
            if height[p1] >= height[p2]:
                p2 -= 1
            else:
                p1 += 1
            area = min(height[p1], height[p2]) * (p2 - p1)
            #print(p1, p2,height[p1],height[p2], area)
            answer = max(answer, area)
        
        return answer

        