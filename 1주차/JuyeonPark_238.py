class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for ele in nums:
            new_lst = nums[:]
            new_lst.pop(nums.index(ele))
            # print(new_lst)
            prod = 1
            for j in range(len(new_lst)):
                prod *= new_lst[j]
            answer.append(prod)
        return answer
