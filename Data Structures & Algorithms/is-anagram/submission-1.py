class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = s.replace(" ","").lower()
        str2 = t.replace(" ","").lower()
        count = [0]*26

        for char in str1:
            count[ord(char)-ord('a')] +=1

        for char in str2:
            count[ord(char)-ord('a')] -=1
        
        for c in count:
            if c != 0:
                return False
        
        return True

        