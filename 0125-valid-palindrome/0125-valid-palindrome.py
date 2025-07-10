import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)
        n = len(s)
        pointer_1 = 0
        pointer_2 = n-1
        print(s)
        while (pointer_1<=pointer_2):
            if s[pointer_1] == s[pointer_2]:
                pointer_1 += 1
                pointer_2 -= 1
            else:
                return False
        return True
