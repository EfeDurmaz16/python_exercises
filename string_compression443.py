from typing import List


class Solution:
        def compress(self, chars: List[str]) -> int:
            for i in range(0, len(chars)):
                count = 1
                while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                    count += 1
                    del chars[i + 1]
                if count > 1:
                    for c in str(count):
                        chars.insert(i + 1, c)
                        i += 1
            return chars

sol = Solution()
# Expected: ["a","2","b","2","c","3"]
print(sol.compress(["a","a","b","b","c","c","c"]))
# Expected: ["a"]
print(sol.compress(["a"]))
# Expected: ["a","b","c"]
print(sol.compress(["a","b","c"]))
# Expected: ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print(sol.compress(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]))  