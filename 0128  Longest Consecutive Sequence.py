class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/longest-consecutive-sequence/
        """

        if len(nums) == 0: return 0                         # edge case where `nums` is empty
        if len(nums) == 1: return 1                         # edge case where `nums` contains only 1 element

        nums = sorted(list(set(nums)))                      # sorted list of set contains only unique numbers

        consecutive = 1                                     # initialize consecutive
        maxcon = 0                                          # initialize maximum consecutive

        for i in range(len(nums)):                          #

            if nums[i] - nums[i-1] == 1:                    # if consecutive numbers exist
                consecutive += 1                            # then update `consecutive` += 1
            else:
                consecutive = 1                             # reset `consecutive` = 1

            maxcon = max(maxcon, consecutive)               # longest consecutive number

        return maxcon


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numset = set(nums)

        longest = 0

        for num in nums:

            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)

        return longest