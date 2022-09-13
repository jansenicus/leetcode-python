class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.
        """
        indices = {}                                  # let indices = {number: index}
        
        for i in range(0, len(nums)):                 
        
            complement = target - nums[i]             # complementary number adds up to the target
                                                      
            if complement in indices:                 # if complementary number exists then return the indices       
                return [i, indices[complement]]
              
            indices[nums[i]] = i                      # register number into indices
        
