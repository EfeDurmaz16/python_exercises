#  Leetcode  151. Reverse Words in a String Solution 

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

#solution = Solution()
#word = solution.reverseWords("the sky is blue")
#   print(word)