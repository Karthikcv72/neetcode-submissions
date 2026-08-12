class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s=""
        for ch in s:
            if(ch.isalnum()):
                new_s+=ch.lower()
        if new_s[::-1]==new_s:
            return True
        return False