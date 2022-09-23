class Solution(object):
    def containsDuplicate(self, nums):
        """
        https://leetcode.com/problems/contains-duplicate/

        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



        Example 1:

        Input: nums = [1,2,3,1]
        Output: true

        Example 2:

        Input: nums = [1,2,3,4]
        Output: false

        Example 3:

        Input: nums = [1,1,1,3,3,4,3,2,4,2]
        Output: true


        Constraints:

        1 <= nums.length <= 105
        -109 <= nums[i] <= 109

        Runtime: 350 ms, faster than 99.82% of Python online submissions for Contains Duplicate.
        Memory Usage: 24.1 MB, less than 8.53% of Python online submissions for Contains Duplicate.

        """

        number_set = set()

        for num in nums:
            if num in number_set:
                return True
            number_set.add(num)

        return False
