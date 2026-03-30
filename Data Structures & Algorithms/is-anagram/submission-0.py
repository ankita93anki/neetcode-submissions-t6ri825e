class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s= s.replace(" ","").lower()
        t= t.replace(" ","").lower()
        return Counter(s) == Counter(t)
        