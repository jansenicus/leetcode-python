class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

        Example 1:

        Input: nums = [-1,0,1,2,-1,-4]
        Output: [[-1,-1,2],[-1,0,1]]
        
        Explanation: 
        nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
        nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
        nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
        The distinct triplets are [-1,0,1] and [-1,-1,2].
        
        Notice that the order of the output and the order of the triplets does not matter.
        """
        
        nums.sort()                                         # sort the numbers
        triplets = []                                       # initialize triplets
        
        for i in range(len(nums) - 2):            

            if i > 0 and nums[i-1] == nums[i]:              # checking from 2nd element onwards
                continue                                    # skips duplicate number
                
            j, k = i + 1, len(nums) - 1                     # `j` starts right next after i,
                                                            # `k` start from last element

            while j < k:                                    # stop when `j` >= `k` 
                
                sum = nums[i] + nums[j] + nums[k]           # define `sum`

                if sum == 0:                                # if `sum` = 0
                    triplet = [nums[i],                     # we got the triplet
                               nums[j],
                               nums[k]]
                               
                    triplets.append( triplet )              # Add triplet to triplets

                    k -= 1                                  # move `k` towards the left

                    while j < k and nums[k] == nums[k+1]:   # if duplicates exists
                        k -= 1                              # move `k` towards the left
                               
                elif sum > 0:                               # if sum more than 0, decrease the number
                    k -= 1                                  # move `k` towards the left
                               
                else:                                       # if sum less than 0, increase the number
                    j += 1                                  # move 'j' towards the right                                  

        return triplets
        
