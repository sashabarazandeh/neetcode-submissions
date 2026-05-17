class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            #key should be the sorted form of the word. if it exists as a key already? append s to the value of the key. if not?
            key = "".join(sorted(s))
            if key in hashMap:
                hashMap[key].append(s)
            else:
                hashMap[key] = [s]
        return list(hashMap.values())
        