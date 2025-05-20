class Solution:
    def isPalindrome(self, s: str) -> bool:
        rmpunct=""
        for c in s:
            if c.isalnum():
                rmpunct += c.lower()
        revStr=rmpunct[::-1]
        return revStr==rmpunct
