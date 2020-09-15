class Solution:
    def search(self, nums: List[int], target: int) -> int:
        print(target)
        print(nums)
        for i in range(0, len(nums)):
            if(nums[i] == target):
                return i
        return -1
        
        
# sort and iterate: easy
# find and then find smallest to the left
