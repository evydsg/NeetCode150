class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) == 0:
            return 0

        length = 0

        for number in nums:
            if number - 1 not in nums:
                count = 1
                temp = number

                while temp + 1 in nums:
                    count += 1
                    temp = temp + 1
                
                length = max(count, length)
        
        return length