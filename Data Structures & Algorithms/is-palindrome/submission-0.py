class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we can use two pointers, 1 at the start,
        # another at the end. we'll iterate them until they reach the middle node
        p1 = 0
        p2 = len(s) - 1
        # compare front and end, if same continue, if not, retrun false
        # for even strings, there wont be middle, we should stop when p1 is > p2 to stop
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
