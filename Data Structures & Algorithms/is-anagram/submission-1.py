class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
           counterS = Counter(s)
           counterT = Counter(t)
           if counterS == counterT:
            return True
        return False
       