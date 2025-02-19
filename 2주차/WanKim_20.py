class Solution(object):
    def isValid(self, s):
        
        n = len(s)
        result = []

        if n % 2 == 1:
            return False

        for i in range(n):
            tmp = len(result)
            
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                result.append(s[i])
            elif s[i] == ')':
                if tmp == 0 or result[tmp-1] != '(': 
                    return False
                result.pop()
            elif s[i] == '}':
                if tmp == 0 or result[tmp-1] != '{': 
                    return False
                result.pop()
            elif s[i] == ']':
                if tmp == 0 or result[tmp-1] != '[': 
                    return False
                result.pop()
                
        if len(result) == 0:
            return True
        return False
        """
        :type s: str
        :rtype: bool
        """
        