class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/

        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Example 1:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Example 2:
        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Example 3:
        Input: nums = [3,3], target = 6
        Output: [0,1]

        Constraints:
        2 <= nums.length <= 104
        -109 <= nums[i] <= 109
        -109 <= target <= 109
        Only one valid answer exists.

        Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

        https://youtu.be/KLlXCFG5TnA
        """
        num_index = {}                                      # let num_index = {number: index}
        
        for idx, num in enumerate(nums):
        
            complementary = target - num                    # define `complementary`
                                                      
            if complementary in num_index:                  # if `complementary` exists
                return [idx, num_index[complementary]]      # we got the index
              
            num_index[num] = idx                            # register number into indices
