#1768 - Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        if(len(word1) == 0):
            return word2
        elif(len(word2) == 0):
            return word1
        elif (len(word1) == 0 and len(word2) == 0):
            return ""
        elif (len(word1)>len(word2)):
            for i in range (0, len(word1)):
                if(i < len(word2)):
                    result += word1[i] + word2[i]
                else:
                    result+= word1[i]
        elif (len(word1)<len(word2)):
            for i in range (0, len(word2)):
                if(i < len(word1)):
                    result += word1[i] + word2[i]
                else:
                    result+= word2[i]

            