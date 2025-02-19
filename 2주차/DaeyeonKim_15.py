class Solution(object):

    
    def check_duplicate(l, answer):
        for temp_list in answer:
            if temp_list == l:
                return True
        return False
            
        
    def threeSum(self, nums):
        number_map = [0 for i in range(20001)] 
        nums.sort() # sort
        answer = []
        for val in nums: #number map in range -10000 ~ 10000
             number_map[val + 10000] += 1

        for idx, val in enumerate(nums):
            for idx2, val2 in enumerate(nums[idx + 1:len(nums)]):
                target = 0 - val - val2
                number_map[val + 10000] -= 1
                number_map[val2 + 10000] -= 1
                temp_answer = sorted([val, val2, target])
                #check duplicate에 temp_answer, answer 두개의 리스트를 파라메터로 넘겼는데 
                #왜 3 arguments given 이라는 에러가 발생하는지 모르겠습니다
                if number_map[target + 10000] >= 1 and not self.check_duplicate(temp_answer, answer):
                    answer.append([val, val2, target])
                number_map[val + 10000] += 1
                number_map[val2 + 10000] += 1
        
        return answer
        