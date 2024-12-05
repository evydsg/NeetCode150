class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        dictionary = {}

        for num in nums:
            if num in dictionary:
                dictionary[num] = True
                return dictionary[num]
            else:
                dictionary[num] = False
        
        return False