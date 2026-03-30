class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''.join([char for char in s if char.isalnum()])
        res = res.lower()
        str1 = res[::-1]
        return res == str1
        