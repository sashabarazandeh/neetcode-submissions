class Solution:
    def search(self, nums: List[int], target: int) -> int:
            low = 0
            high = len(nums) - 1

            while low <= high:
                # Clean way to find the middle integer index
                midindex = (low + high) // 2
                midvalue = nums[midindex]
                
                if target > midvalue:
                    # Target is in the right half, shift the low boundary up
                    low = midindex + 1
                elif target < midvalue:
                    # Target is in the left half, shift the high boundary down
                    high = midindex - 1
                else:
                    # Target matches midvalue perfectly! Return original index
                    return midindex
                    
            # If the pointers cross, the target does not exist in the array
            return -1
