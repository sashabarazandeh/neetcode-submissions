class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        answer = []
        for i, n in enumerate(nums):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            else:
                hashMap[n] = i
        return []

