class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """

        https://leetcode.com/problems/3sum/

        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

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
        
        nums.sort()                                             # sort the numbers
        triplets = []                                           # initialize triplets
        
        for i in range(0, len(nums) - 2):

            if i > 0 and nums[i-1] == nums[i]:                  # checking from 2nd element onwards
                continue                                        # skips duplicate number
                
            l = i + 1                                           # `l` starts from the second element,
            r = len(nums) - 1                                   # `r` start from the last element

            while l < r:

                triplet = (nums[i], nums[l], nums[r])           # define `triplet`

                current_sum = sum(triplet)                      # `current_sum`

                if current_sum < 0:                             # if `current_sum` < 0,
                    l += 1                                      # increase `l`

                elif current_sum > 0:                           # if `current_sum` > 0,
                    r -= 1                                      # decrease `r`

                else:                                           # if `sum` = 0

                    triplets.append(triplet)                    # Add triplet to triplets

                    r -= 1                                      # decrease `r`, keep moving

                    while l < r and nums[r] == nums[r+1]:       # skips duplicate number
                        r -= 1                                  # decrease `r`, keep moving

        return triplets
        
