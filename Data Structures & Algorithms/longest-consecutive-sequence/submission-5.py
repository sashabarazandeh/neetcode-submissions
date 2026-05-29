class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        best = 0
        current = 0
        for i in nums:
            if i-1 not in newSet: #start of a consectuive list
                length = 1
                while i + length in newSet:
                    length += 1
                best = max(best, length)
        return best
                