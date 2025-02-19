class Solution(object):
    def hammingWeight(self, n):
        binary = bin(n)[2:] # returns in format 0b#### so discard the first two characters
        return binary.count('1') #count number of 1s in the string
        