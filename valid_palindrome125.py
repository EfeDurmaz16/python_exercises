class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        i = 0
        while i < len(s):
            if s[i].isalnum():
                st.append(s[i].lower())
            i += 1
        len_st = len(st)
        
        for i in range(len_st // 2):
            if st[i] != st[len_st - i - 1]:
                return False
        return True

# Test Cases
sol = Solution()
# Expected: True
print(sol.isPalindrome('racecar'))


