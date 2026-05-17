class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        freqs = [[] for _ in range(len(nums) + 1)]
        for key, val in hashMap.items():
            freqs[val].append(key)
        
        result = []
        for i in range(len(freqs) - 1, 0, -1):
            for num in freqs[i]:
                result.append(num)
                if len(result) == k:
                    return result
