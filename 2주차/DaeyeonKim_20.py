class Solution(object):
    def isValid(self, s):
        from collections import deque
        stack = deque()

        for p in s:
            if p == '(' or p == '[' or p == '{': #open parantheses > push
                stack.append(p)
            else:
                if not stack: #pop in a empty stack > false
                    return False
                pop = stack.pop()
                if pop == '(' and p == ')':
                    print("1")
                    continue
                elif pop == '[' and p == ']':
                    print("2")
                    continue
                elif pop == '{' and p == '}':
                    print("3")
                    continue
                else:
                    return False

        if stack: #not empty > false
            return False
        return True