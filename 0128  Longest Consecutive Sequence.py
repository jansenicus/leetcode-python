class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/

        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4

        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

        Example 2:

        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:

        0 <= nums.length <= 105
        -109 <= nums[i] <= 109

        """

        if len(nums) == 0: return 0                         # edge case where `nums` is empty
        if len(nums) == 1: return 1                         # edge case where `nums` contains only 1 element

        nums = sorted(list(set(nums)))                      # sorted list of set contains only unique numbers

        consecutive = 1                                     # initialize consecutive
        longest = 0                                         # initialize longest consecutive

        for i in range(len(nums)):                          #

            if nums[i] - nums[i-1] == 1:                    # if consecutive numbers exist
                consecutive += 1                            # then update `consecutive` += 1
            else:
                consecutive = 1                             # reset `consecutive` = 1

            longest = max(longest, consecutive)             # longest consecutive number

        return longest


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        another solution by neetcode
        """

        number_set = set(nums)

        longest = 0

        for num in nums:

            if (num - 1) not in number_set:
                streak = 0
                while (num + streak) in number_set:
                    streak += 1
                longest = max(longest, streak)

        return longest
