class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums)//3
        # probably want to use a hashmap here.
        hashMap = {}
        
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        result = []
        for i in hashMap:
            if hashMap[i] > target:
                result.append(i)
        return result