def productExceptSelf(nums):
    answer = []

    for self_idx in range(len(nums)):
        product = 1
        for idx, num in enumerate(nums):
            if self_idx != idx:
                product *= num
        answer.append(product)

    return answer
