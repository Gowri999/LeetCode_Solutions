class Solution:
    def gcdOfStrings(self, str1, str2):

        # Check if both strings have the same pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD manually
        a = len(str1)
        b = len(str2)

        while b:       
            a, b = b, a % b

        return str1[:a]
