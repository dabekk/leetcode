class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        num_set = set(nums)
        overall_max = 1
        for num in num_set:
            current_max = 1
            if (num - 1) not in num_set:
                while num + 1 in num_set:
                    current_max += 1
                    num += 1
            overall_max = max(overall_max, current_max)
        
        return overall_max
