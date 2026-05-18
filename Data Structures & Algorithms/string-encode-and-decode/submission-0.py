class Solution:

    def encode(self, strs: List[str]) -> str:
        #first we need to encode the list, so loop the list
        # and then count the lenght of each s in strings, create a new string "n#s"
        encodedStr = ""
        for s in strs:
            current = f"{len(s)}#{s}"
            encodedStr += current
        return encodedStr

    def decode(self, s: str) -> List[str]:
        #now that the string is joined by "n#string" pattern
        #we need to loop through each character and create substrings at sepcific spots.
        #once we reach a # as the next char, we know we have the lenght, we call an inner for loop
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            current = ""
            for i in range(j+1, j+1+length, 1):
                current += (s[i])
            result.append(current)
            i = j+1+length
        return result
                

