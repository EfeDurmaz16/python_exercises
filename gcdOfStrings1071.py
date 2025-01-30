class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        if not str1:
            return str2
        if not str2:
            return str1

        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2)
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str1, str2[len(str1):])
        else:
            return str1

sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC")) # ABC
print(sol.gcdOfStrings("ABABAB", "ABAB")) # AB
print(sol.gcdOfStrings("LEET", "CODE")) # ""
print(sol.gcdOfStrings("ABCDEF", "ABC")) # ""
print(sol.gcdOfStrings("ABC", "ABCDEF")) # ""