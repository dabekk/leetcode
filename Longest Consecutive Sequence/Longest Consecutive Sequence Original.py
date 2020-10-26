if(len(nums) > 0):         # account for list being empty
            curr_count = 1
            curr_max = 1
        else:
            curr_count = 0
            curr_max = 0
        
        print(nums)
        for i in range (len(nums) - 1):
            curr_num = nums[i]
            next_num = nums [i+1]
            
            if(curr_num == next_num-1):
                curr_count += 1
                if(curr_count > curr_max):
                    curr_max = curr_count

        return curr_max
    
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        for i in range(len(nums)):
            if(nums[i] >= 0):
                break
            
        negatives = nums[:i]
        positives = nums[i:]
        print(negatives)
        print(positives)
        
        max_neg = self.longestConsecutiveCount(negatives)
        max_pos = self.longestConsecutiveCount(positives)
        if(max_neg > max_pos):
            return max_neg
        else:
            return max_pos
