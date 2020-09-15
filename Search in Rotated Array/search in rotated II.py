class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        print(target)
        print(nums)
        for i in range(0, len(nums)):
            if(nums[i] == target):
                return True
        return False
