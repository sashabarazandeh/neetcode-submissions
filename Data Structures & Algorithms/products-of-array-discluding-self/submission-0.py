class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        output = [1] * len(nums)
        suffix = [1] * len(nums) #1, 2, 3 ,4
                    # prefix: 1, 1, 2, 6
                    # suffix: 24, 12, 4, 1
        for i in range(1, len(nums)):           # start at 1, skip index 0
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(len(nums) - 2, -1, -1):  # start at n-2, skip last index
            suffix[i] = suffix[i+1] * nums[i+1]
            
        for i in range(len(nums)):
            output[i] = prefix[i] * suffix[i]
        return output
                

            